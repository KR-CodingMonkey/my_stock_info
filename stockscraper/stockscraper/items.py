import scrapy


class StockscraperItem(scrapy.Item):
    # - 데이터를 읽어온 시간
    # - 현재 거래량
    # - 현재 가격
    # - 최고가
    # - 최저가
    # - 종목 코드

    stock_num = scrapy.Field() # 종목코드
    max_price = scrapy.Field() # 최고가
    min_price = scrapy.Field() # 최저가
    current_price = scrapy.Field() # 현재가
    trading_volume = scrapy.Field() # 거래량
    created_at = scrapy.Field() # 데이터를 읽어온 시간
