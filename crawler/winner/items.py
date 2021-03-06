# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

#import scrapy
from scrapy import Item,Field


class WinnerItem(Item):
    zuone_author_name = Field()
    zuone_author_img = Field()
    zuone_name = Field()
    zuone_img = Field()
    zuone_url = Field()
    zuone_piao = Field()

class CookbookItem(Item):
    itemid = Field()
    tip = Field()
    matter = Field()
    steps = Field()

class MaterialItem(Item):
    name = Field()
    url = Field()
    img = Field()
    effect = Field()
