#-*-coding:UTF-8-*-
from scrapy.spider import Spider
from scrapy.selector import Selector  
from scrapy.http import Request
from winner.items import MaterialItem

class MaterialSpider(Spider):
    name = "material"
    allowed_domains = ["douguo.com"]
    start_urls = ["http://www.douguo.com/shicai"]
    base_url = 'http://www.douguo.com'

    def parse(self, response):
        #print response.body
        sel = Selector(response)
        all_link = sel.xpath('//div[@class="caiputo2 mt30"]/h2/a/@href')
        for link in all_link:
            url = self.base_url+link.extract()
            #print url
            yield Request(url,meta={},callback=self.parse2)

    def parse2(self, response):
        sel = Selector(response)
        _a = sel.xpath('//div[@class="caicontr"]/div/a')
        for a in _a:
            m = MaterialItem()
	    m['name'] = a.xpath('img/@alt').extract()[0]
	    m['img'] = a.xpath('img/@src').extract()[0]
	    m['url'] = a.xpath('@href').extract()[0]
            yield Request(m['url']+'/effect',meta={'item':m},callback=self.parse_effect)

    def parse_effect(self, response):
        body = Selector(response)
        effect = body.xpath('//div[@id="shicaijieshao"]').extract()
        material = response.meta['item']
        material['effect'] = effect
        yield material

