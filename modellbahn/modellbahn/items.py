# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class ModellbahnItem(scrapy.Item):
    # Alle Attribute hier als Feld definieren:
    # Attribute aus Request
    vorbild = scrapy.Field()
    artnr  = scrapy.Field()
    art  = scrapy.Field()
    epoche = scrapy.Field()
    modell = scrapy.Field()
    betrieb = scrapy.Field()
    bilder = scrapy.Field()
    kataloge = scrapy.Field()
    # Attribute per Code
    ts = scrapy.Field()
    # Attribute für Download von Images
    image_urls = scrapy.Field()
    images = scrapy.Field()
