# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy


class ModellbahnItem(scrapy.Item):
    # Alle Attribute hier als Feld definieren:
    url  = scrapy.Field()
    # Attribute für Dateninhalte aus response
    vorbild = scrapy.Field()
    artnr  = scrapy.Field()
    art  = scrapy.Field()
    epoche = scrapy.Field()
    modell = scrapy.Field()
    betrieb = scrapy.Field()
    bilder = scrapy.Field()
    kataloge = scrapy.Field()
    # Zusatz-Attribute per Code gesetzt
    # Timestamp
    ts = scrapy.Field()
    # Attribute für Download von Images (von scrapy so gefordert!)
    image_urls = scrapy.Field()
    images = scrapy.Field()

    def createEmptyItem(self):
        self['vorbild'] =''
        self['artnr'] = 'unbekannt'
        self['vorbild'] = ''
        self['art'] = ''
        self['epoche'] = ''
        self['modell'] = ''
        self['betrieb'] = ''
        self['kataloge'] = ''
        self['bilder'] = []
        self['image_urls'] = []
