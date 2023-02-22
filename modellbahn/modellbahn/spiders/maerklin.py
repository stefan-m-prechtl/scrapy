import scrapy
from modellbahn.items import ModellbahnItem

class HelloworldSpider(scrapy.Spider):
    name = 'maerklin'
    baseUrl = 'https://www.maerklin.de/de/produkte/details/article/'

    def start_requests(self):
        #urls =['https://www.maerklin.de/de/produkte/details/article/30000']
        urls = self.loadUrls()
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def loadUrls(self):
        urls = []
        with open('loks.csv') as datafile:
            urls = [ self.baseUrl + line.strip() for line in datafile]
        return urls

    def parse(self, response):
        # mit Itemloader hat es nicht geklappt die Biler als nested-Array zu laden --> Item manuell erzeugen
        item = ModellbahnItem()
        item['vorbild'] = response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[2]/div/p/text()').get().strip()
        item['artnr'] = response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr/td/span/text()').get().strip()
        item['art'] = response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr[4]/td/text()').get().strip()
        item['epoche'] = response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr[3]/td/text()').get().strip()
        item['modell'] = response.css('.long-text::text').get().strip()
        if response.css('.long-text2::text').get():
            item['betrieb'] = response.css('.long-text2::text').get().strip()
        item['kataloge'] = [katalog for katalog in response.css('.left-15 span *::text').getall()]
        item['bilder'] = [bild.attrib['href'] for bild in response.css('div.product-slider-big div a')]
        item['image_urls'] = [bild.attrib['href'] for bild in response.css('div.product-slider-big div a')]

        return item

        # yield{
        #     'Vorbild' : response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[2]/div/p/text()').get().strip(),
        #     'ArtNr': response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr/td/span/text()').get().strip(),
        #     'Epoche': response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr[3]/td/text()').get().strip(),
        #     'Art': response.xpath('/html/body/container/div[1]/div[1]/div[2]/div[4]/div/div[2]/table/tr[4]/td/text()').get().strip(),
        #     'Modell': response.css('.long-text::text').get().strip(),
        #     'Bilder' : [ bild.attrib['href'] for bild in response.css('div.product-slider-big div a')]
        # }
