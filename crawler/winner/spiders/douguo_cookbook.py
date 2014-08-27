#-*-coding:UTF-8-*-
from scrapy.spider import Spider
from scrapy.selector import Selector  
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from winner.items import CookbookItem
import json
import re

class Douguo_cookbookSpider(Spider):
    name = "douguo_cookbook"
    allowed_domains = ["douguo.com"]
    start_urls = ["http://www.douguo.com/huodong/cdbaking/show/2/"]
    re_id = re.compile('cookbook/(\d+).html')

    def parse(self, response):
        #winners = json.loads(open('winner.json','r').read())[:2]
        winners = json.loads(open('winner.json','r').read())
        for w in winners:
            itemid = self.re_id.findall(w['zuone_url'])[0]
            yield Request(w['zuone_url'],meta={'itemid':itemid},callback=self.parse2)

    def parse2(self, response):
        sel = HtmlXPathSelector(response)
        div = sel.xpath('//div[@class="recinfo"]')

        tip = div.xpath('div/div[@class="xtip"]/text()').extract()
        if tip:tip = tip[0]

        matter = []
        matter_table = div.xpath('div/table[@class="retamr"]')
        for td in matter_table.xpath('//td'):
            matt_name = td.xpath('span[1]/label/text()').extract()
            if matt_name :
                matt_name = matt_name[0]
            else:
                matt_name = td.xpath('span[1]/a/text()').extract()
                if matt_name :
                    matt_name = matt_name[0]

            matt_amount = td.xpath('span[2]/text()').extract()
            if matt_amount :matt_amount = matt_amount[0]

            if matt_name and matt_amount :
                matter.append({'name':matt_name,'amount':matt_amount})
        steps = div.xpath('div/div[@class="step clearfix"]/div').extract()
        #print len(steps)
        #print steps[0]
        cb = CookbookItem()
        cb['itemid'] = response.meta['itemid']
        cb['tip'] = tip
        cb['matter'] = matter
        cb['steps'] = steps
        yield cb
        #for zuone in div:
        #    zuone_data = WinnerItem()
        #    zuone_data['zuone_author_name'] = zuone.xpath('div[@class="zphed"]/a/@title').extract()[0]
        #    zuone_data['zuone_author_img'] = zuone.xpath('div[@class="zphed"]/a/img/@src').extract()[0]
        #    zuone_data['zuone_name'] = zuone.xpath('div[@class="rcname"]/a/@title').extract()[0]
        #    zuone_data['zuone_img'] = zuone.xpath('div[@class="imgxc"]/a/img/@src').extract()[0]
        #    zuone_data['zuone_url'] = 'http://www.douguo.com'+zuone.xpath('div[@class="imgxc"]/a/@href').extract()[0]
        #    zuone_data['zuone_piao'] = zuone.xpath('div[@class="piaonum"]/font/text()').extract()[0]
        #    yield zuone_data
