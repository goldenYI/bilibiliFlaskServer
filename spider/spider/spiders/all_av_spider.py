# coding:utf-8

import scrapy
from scrapy_splash import SplashRequest
import re


class all_av_spider(scrapy.Spider):
    name = "all_av_spider"
    allowed_domains = "http://www.bilibili.com/"
    start_urls = [
        "http://www.bilibili.com/video/av8250661/"
    ]
    script = """
        function main(splash)
            assert(splash:go(splash.args.url))
            splash:runjs("$('#index_nav > .nav-list > :nth-child(13)').click()")
            splash:wait(2)
            return {
                html = splash:html()
            }
        end
        """
    splash_args = {
        'html': 1,
        'images': 0,
        'script': 1,
        'lua_source': script,
    }
    items = []  # 定义items空集

    def __init__(self, filename=None, **kwargs):
        super(all_av_spider, self).__init__(**kwargs)
        if filename is not None:
            self.filename = filename
        else:
            self.filename = self.name
    def parse(self, response):
        str = response.xpath("//div[@id='bofqi']/script/text()").extract()[0]
        print str
        print re.findall('cid=(\d+)&aid=(\d+)',str)

