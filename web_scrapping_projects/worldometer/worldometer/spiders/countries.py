import scrapy


class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]
    start_urls = [
        "https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        cntrs = response.xpath('//td/a')

        for cntr in cntrs:
            name = cntr.xpath('.//text()').get()
            link = cntr.xpath('.//@href').get()

            yield response.follow(url=link, callback=self.parse_country_link, meta={'country_name': name})

    def parse_country_link(self, response):
        name = response.request.meta['country_name']
        rows = response.xpath(
            '(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        for row in rows:
            year = row.xpath('.//td[1]/text()').get()
            population = row.xpath('.//td[2]/strong/text()').get()
            yield {
                'country_name': name,
                'year': year,
                'population': population
            }
