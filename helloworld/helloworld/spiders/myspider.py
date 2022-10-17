import scrapy

class HelloworldSpider(scrapy.Spider):
    name = "maerklin"

    def start_requests(self):
        urls = [
            'https://www.maerklin.de/de/produkte/details/article/30000',
            'https://www.maerklin.de/de/produkte/details/article/36244']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        self.logger.info('Vorbild: ' + response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[2]/div/p/text()').get())
        self.logger.info('Art.Nr: ' + response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr/td/span/text()').get())
        self.logger.info('Epoche: ' + response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr[3]/td/text()').get())
        self.logger.info('Art: ' + response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr[4]/td/text()').get())
        self.logger.info('Modell: ' + response.css('.long-text::text').get())
        bilder = response.css('div.product-slider-big div a')
        for bild in bilder:
            self.logger.info("Bild: " + bild.attrib['href'])
        pass
