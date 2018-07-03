# -*- coding: utf-8 -*-
import scrapy
from pathlib import Path
from zhaopin.items import ZhaopinItem


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['zhaopin.baidu.com']
    path = Path(r'D:\onedrive\Python_Projects\zhaopin_spider\links.txt')
    start_urls = path.open().readlines()

    def parse(self, response):
        def xpath2item(expression, item_key):
            item[item_key] = response.xpath(expression).extract_first()
        
        item = ZhaopinItem()

        node = "//div[@class='top-txt']"
        xpath2item(f"{node}/span[contains(@class, 'title')]/text()", 'position')
        xpath2item(f"{node}/span[@class='salary']", 'salary')

        node = "//ul[@class='list-left left']"
        xpath2item(f"{node}//span[@class='area']/../text()", 'area')
        xpath2item(f"{node}//span[@class='xueli']/../text()", 'education')
        xpath2item(f"{node}//span[@class='minge']/../text()", 'experience')
        xpath2item(f"{node}//span[@class='num']/../text()", 'number')

        node = "//div[@class='abs']"
        xpath2item(f"{node}/p[contains(text(), '职位类型')]/text()", 'type_')
        xpath2item(f"{node}/p[contains(text(), '发布时间')]/text()", 'pubdate')
        xpath2item(f"{node}/p[contains(text(), '有效日期')]/text()", 'validate')
        xpath2item(f"{node}/p[@class='duty duty-box']/text()", 'duty')

        node = "//div[@class='details']"
        xpath2item(f"{node}//div[@class='right txt']/p/text()", 'company')
        xpath2item(f"{node}/p[contains(text(), '性质')]/text()", 'co_property')
        xpath2item(f"{node}/p[contains(text(), '规模')]/text()", 'co_scale')
        xpath2item(f"{node}/p[contains(text(), '类型')]/text()", 'co_type')
        xpath2item(f"{node}/p[contains(text(), '工作地点')]/text()", 'address')

