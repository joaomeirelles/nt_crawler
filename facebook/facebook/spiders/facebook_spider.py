import scrapy


class facebookSpider(scrapy.Spider):
    name = "facebook"

    def start_requests(self):
        urls = [
            'https://www.facebook.com/<some_user_name>',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        content = response.xpath('//*[@id="profile_timeline_tiles_unit_pagelets_friends"]')
        print '-'*80
        print content
        print '-'*80