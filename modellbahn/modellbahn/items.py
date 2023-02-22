# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class ModellbahnItem(scrapy.Item):
    # Alle Attribute hier als Feld definieren
    vorbild = scrapy.Field()
    artnr  = scrapy.Field()
    epoche = scrapy.Field()
    modell = scrapy.Field()
    bilder = scrapy.Field()
