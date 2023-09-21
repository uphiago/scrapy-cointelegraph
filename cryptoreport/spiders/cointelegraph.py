import scrapy
import re
from scrapy_splash import SplashRequest

class CointelegraphSpider(scrapy.Spider):
    name = 'cointelegraph'
    start_urls = ['https://www.cointelegraph.com']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_response, args={'wait': 3})

    def parse_response(self, response):
        links = response.css('.post-card__title-link::attr(href)').getall()
        for link in links:
            absolute_url = response.urljoin(link)
            if re.search("/news/", absolute_url):
                yield SplashRequest(url=absolute_url, callback=self.parse_news_article, args={'wait': 2})
            elif re.search("/magazine/", absolute_url):
                yield SplashRequest(url=absolute_url, callback=self.parse_magazine_article, args={'wait': 2})

    def clean_text(self, text):
        if text is not None:
            text = text.strip()
            text = text.replace('\u2018', "'")  # Replace U+2018 "‘" with "'"
            text = text.replace('\u2019', "'")  # Replace U+2019 "’" with "'"
            text = text.replace('\u00a0', " ")  # Replace U+00a0 (non-breaking space) with a regular space
            text = text.replace('\uFE0F', "")  # Remove U+FE0F
            text = text.replace('\u2013', "-")  # Replace U+2013 "–" with "-"
            text = text.replace("\\", "")  # Remove backslashes
            text = re.sub(' +', ' ', text)  # Replace multiple spaces with a single space using regex
        return text

    def parse_news_article(self, response):
        title = self.clean_text(response.css('.post__title::text').get())
        subtitle = self.clean_text(response.css('.post__lead::text').get())
        author = self.clean_text(response.css('div.post-meta__author-name::text').get())
        timestamp = response.css('time::attr(datetime)').get()
        content = ' '.join(response.css(".post-content p::text, .post-content p a::text, .post-content blockquote::text, .post-content li::text").getall())
        content = self.clean_text(content)

        yield {
            'title': title,
            'subtitle': subtitle,
            'author': author,
            'timestamp': timestamp,
            'content': content,
            'url': response.url
        }
    
    def parse_magazine_article(self, response):
        title = self.clean_text(response.css('div.article-top__title.display1 h1::text').get())
        subtitle = self.clean_text(response.css('h2.article-top__title__subtitle::text').get())
        author = self.clean_text(response.css('div.article-top__props.props span.props__item a::text').get())
        timestamp = response.css('div.article-top__props.props span.props__item:nth-child(3)::text').get()
        content = ' '.join(response.css("div.article__inner.body-l p::text").getall())
        content = self.clean_text(content)

        yield {
            'title': title,
            'subtitle': subtitle,
            'author': author,
            'timestamp': timestamp,
            'content': content,
            'url': response.url
        }