# coding:utf-8

import scrapy
from scrapy_splash import SplashRequest
from spider.items import HomeItem
import re
class home_technology_spider(scrapy.Spider):

    name = "home_technology_spider"
    allowed_domains = "http://www.bilibili.com/"
    start_urls = [
        "http://www.bilibili.com"
    ]
    script = """
        function main(splash)
            assert(splash:go(splash.args.url))
            splash:runjs("$('#index_nav > .nav-list > :nth-child(7)').click()")
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
    def __init__(self, **kwargs):
        super(home_technology_spider, self).__init__(**kwargs)
        print "启动爬虫"

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='execute',
                                args={'lua_source': self.script})

    def parse(self, response):
        music_ul = response.xpath(
            "//div[@id='b_technology']//ul[@class='vidbox v-list']//li"
        )
        for sel in music_ul:
            item = HomeItem()
            item['data_txt'] = sel.xpath("@data-txt")[0].extract()
            item['data_up'] = sel.xpath("@data-up")[0].extract()
            item['data_gk'] = sel.xpath("@data-gk")[0].extract()
            item['data_tg'] = sel.xpath("@data-tg")[0].extract()
            item['data_dm'] = sel.xpath("@data-dm")[0].extract()
            a = sel.xpath("div/a[@class='preview cover-preview']")
            item['data_title'] = a.xpath("img/@alt")[0].extract()
            item['data_img'] = 'http:'+a.xpath("img/@src")[0].extract()
            item['data_av'] = re.findall('\/video\/av(.*)\/', a.xpath("@href")[0].extract())[0]
            self.items.append(item)
        return self.items  # 返回项目