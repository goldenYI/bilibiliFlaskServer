# coding:utf-8

import scrapy
from scrapy_splash import SplashRequest

class home_music_spider(scrapy.Spider):
    name = "home_music_spider"
    allowed_domains = "http://www.bilibili.com/"
    start_urls = [
        "http://www.bilibili.com"
    ]
    script = """
        function main(splash)
            splash:go(splash.args.url)
            splash:runjs("window.scrollTo(0,99999)")
            splash:wait(15)
            return {
                html = splash:html(),
                url = "asduhasiudhasd",
            }
        end
    """
    splash_args = {
        'html': 1,
        'images': 0,
        'lua_source': script
    }
    def __init__(self):
        print "启动爬虫"

    def start_requests(self):
        print '-----------start_requests----------'
        for url in self.start_urls:
            yield SplashRequest(url,
                                self.parse_result,
                                args=self.splash_args)

    def parse_result(self, response):
        print '-----------videolist----------'
        music_ul = response.xpath(
            "//div[@id='b_music']/div[@class='b-section-body']"
            "/div[@class='b-l']/div[@class='b-body']/ul[@class='vidbox v-list']"
        )
        counter = 0
        for sel in music_ul.xpath("//li/@data-txt"):
            print '----------%s-----------' % counter
            print sel.extract()
            counter += 1
