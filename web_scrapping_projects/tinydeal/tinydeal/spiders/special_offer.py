import scrapy


class SpecialOfferSpider(scrapy.Spider):
    name = "special_offer"
    allowed_domains = ["www.tinydeals.co"]
    start_urls = [
        "https://www.tinydeals.co/product-category/smart-phones-tablets"]

    def parse(self, response):
        for product in response.xpath("//div[@class = 'columns-5 products col_wrap_fifth eq_grid pt5 rh-flex-eq-height']/div/div[1]/div"):
            yield {
                "product_name": product.xpath(".//h3/a/text()").get(),
                "product_price": {
                    "low_range": product.xpath(".//div/div/div/span/span/span[1]/bdi/text()").get(),
                    "high_range": product.xpath(".//div/div/div/span/span/span[2]/bdi/text()").get()
                },
                "product_url": product.xpath(".//h3/a/@href").get()
            }

        next_page = response.xpath(
            "//a[@class = 'next page-numbers']/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
