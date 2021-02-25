import scrapy
# from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
from stockscraper.items import StockscraperItem
from datetime import datetime

class StockBotsSpider(scrapy.Spider):
    name = 'stock_bots'
    i = 0

    allowed_domains = ['finance.naver.com/item/sise.nhn?code=005930']
    start_urls = ['https://finance.naver.com/item/sise.nhn?code=005930']

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse)

    def parse(self, response):
        self.i = self.i+1

        stock_num = response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()
        max_price = response.xpath('//*[@id="_high"]/text()').extract()
        min_price = response.xpath(' //*[@id="_low"]/text()').extract()
        current_price = response.xpath('//*[@id="content"]/div[2]/div[1]/table/tbody/tr[4]/td[2]/span/text()').extract()
        trading_volume = response.xpath('//*[@id="_quant"]/text()').extract()
        created_at = datetime.now()

        stock_info = StockscraperItem()
        stock_info['stock_num'] = stock_num[0]
        stock_info['max_price'] = max_price[0]
        stock_info['min_price'] = min_price[0]
        stock_info['current_price'] = current_price[0]
        stock_info['trading_volume'] = trading_volume[0]
        stock_info['created_at'] = created_at.strftime('%Y-%m-%d %H:%M:%S')

        # print(stock_info)
        return stock_info

