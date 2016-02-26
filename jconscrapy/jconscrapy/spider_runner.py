from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import  get_project_settings
from jconscrapy.jconscrapy.spiders.configurable_spider import  ConfigurableSpider
import os
os.environ["SCRAPY_SETTINGS_MODULE"] = "jconscrapy.jconscrapy.settings"
process = CrawlerProcess(get_project_settings())
process.crawl(ConfigurableSpider,*(None, './configs/young_hungry_free.json'))
process.start()
print 'Finished'