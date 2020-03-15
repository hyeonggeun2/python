import scrapy
class QuotesSpider(scrapy.Spider):
    name = "festa"
    allowed_domains = ["festa.io"]
    start_urls = [
        "https://festa.io/events"
    ]
    
    # parse 는 scrapy 의 디폴트 콜백 함수이다.
    # start_urls 에서 response 를 받으면 parse 콜백함수를 호출. response를 인자로 parse()에 전달
    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall()
            }
        # next_page = response.css('li.next a::attr(href)').get()
        for a in response.css('li.next a::attr(href)'):
            yield response.follow(a, callback=self.parse)