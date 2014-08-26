#-*-coding:UTF-8-*-
from scrapy.spider import BaseSpider
from scrapy.selector import Selector  
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from winner.items import WinnerItem

class Douguo_winnerSpider(BaseSpider):
    name = "douguo_winner"
    allowed_domains = ["douguo.com"]
    start_urls = ["http://www.douguo.com/huodong/cdbaking/show/2/"]

    def parse(self, response):
        for i in xrange(34):
            page = str(i*24)
            if page == '0':page=''
            yield Request(self.start_urls[0]+page,meta={},callback=self.parse2)

    def parse2(self, response):
        sel = HtmlXPathSelector(response)
        div = sel.xpath('//div[@class="zuone"]')
        for zuone in div:
            zuone_data = WinnerItem()
            zuone_data['zuone_author_name'] = zuone.xpath('div[@class="zphed"]/a/@title').extract()[0]
            zuone_data['zuone_author_img'] = zuone.xpath('div[@class="zphed"]/a/img/@src').extract()[0]
            zuone_data['zuone_name'] = zuone.xpath('div[@class="rcname"]/a/@title').extract()[0]
            zuone_data['zuone_img'] = zuone.xpath('div[@class="imgxc"]/a/img/@src').extract()[0]
            zuone_data['zuone_url'] = 'http://www.douguo.com'+zuone.xpath('div[@class="imgxc"]/a/@href').extract()[0]
            zuone_data['zuone_piao'] = zuone.xpath('div[@class="piaonum"]/font/text()').extract()[0]
            yield zuone_data
