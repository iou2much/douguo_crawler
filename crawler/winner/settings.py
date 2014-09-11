# -*- coding: utf-8 -*-

# Scrapy settings for winner project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'winner'

SPIDER_MODULES = ['winner.spiders']
NEWSPIDER_MODULE = 'winner.spiders'
DOWNLOAD_DELAY = 0.3    # 250 ms of delay
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'winner (+http://www.yourdomain.com)'
