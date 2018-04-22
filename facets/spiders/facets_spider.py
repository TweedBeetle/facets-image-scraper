import scrapy
import urllib

class FacetsSpider(scrapy.Spider):
    name = 'facets'

    allowed_domains = ['facets.la']

    start_urls = list()

    url_base = 'http://www.facets.la'

    for year in [2013, 2014]:
        for day in range(1, 366):
            url = '{}/{}/{}/'.format(url_base, year, day)
            start_urls.append(url)

    def parse(self, response):
        exists = int(response.xpath('boolean(//*[text()[contains(., "Download Wallpaper")]])').extract_first())
        if not exists:
            print 'doesn\'t exist'
            return
        image_url = response.xpath('//*[text()[contains(., "Download Wallpaper")]]/@href').extract_first()
        name = response.xpath('string(/html/body/div[@id="central"]/div[@id="content"]/div[3]/h1)').extract_first()
        name = name.replace('/', '-')
        urllib.urlretrieve(image_url, 'images/'+name+'.jpg')
        print 'downloaded {}'.format(name)