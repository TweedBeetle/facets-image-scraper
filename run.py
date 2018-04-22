import os, shutil
from scrapy.crawler import CrawlerProcess
from facets.spiders.facets_spider import FacetsSpider

if __name__ == '__main__':

    try:
        shutil.rmtree('images')
    except:
        pass

    os.mkdir('images')

    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
    })

    process.crawl(FacetsSpider)
    process.start()

