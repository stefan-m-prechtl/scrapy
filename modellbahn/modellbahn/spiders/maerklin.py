import scrapy
from scrapy.loader import ItemLoader
from modellbahn.modellbahn.items import ModellbahnItem

class HelloworldSpider(scrapy.Spider):
    name = "maerklin"

    def start_requests(self):
        urls = [
            'https://www.maerklin.de/de/produkte/details/article/4314',
            'https://www.maerklin.de/de/produkte/details/article/30000',
            'https://www.maerklin.de/de/produkte/details/article/36244']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        loader = ItemLoader(item=ModellbahnItem(), response=response)
        loader.add_css('modell', '.long-text::text')
        loader.add_xpath('epoche','/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr[3]/td/text()')
        result = loader.load_item()
        return result
        

        # yield{
        #     'Vorbild' : response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[2]/div/p/text()').get().strip(),
        #     'ArtNr': response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr/td/span/text()').get().strip(),
        #     'Epoche': response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr[3]/td/text()').get().strip(),
        #     'Art': response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr[4]/td/text()').get().strip(),
        #     'Modell': response.css('.long-text::text').get().strip(),
        #     'Bilder' : [ bild.attrib['href'] for bild in response.css('div.product-slider-big div a')]
        # }
