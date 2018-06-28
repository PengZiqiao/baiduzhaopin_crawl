from chrospider import ChroSpider
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path


class Spider:
    spider = ChroSpider()
    path = Path('links.txt')

    def query_page(self, keyword, city):
        self.spider.driver.get(f'https://zhaopin.baidu.com/quanzhi?query={keyword}&city={city}')
        self.spider.wait(30).until(EC.presence_of_element_located(('class name', 'logo')))

    @property
    def district_list(self):
        node = self.spider.driver.find_element_by_class_name('filter-district')
        elements = node.find_elements_by_tag_name('a')
        for each in elements[1:]:
            yield each.text

    def get_links(self):
        elements = self.spider.driver.find_elements_by_class_name('line-bottom')
        for each in elements:
            yield each.get_attribute('href')

    def write_links(self):
        with open(self.path, 'a+') as f:
            f.writelines((line+'\n' for line in  self.get_links()))

    def change_district(self, dist):
        self.spider.click(dist)
        self.__wait_loaded()

    def next_page(self):
        self.spider.driver.find_element_by_link_text('下一页').click()
        self.__wait_loaded()

    def __wait_loaded(self):
        self.spider.wait(2).until(EC.visibility_of_element_located(('id', 'data-loading')))
        self.spider.wait(10).until(EC.invisibility_of_element_located(('id', 'data-loading')))

    def run(self):
        for dist in self.district_list:
            self.change_district(dist)
            self.write_links()

            while self.spider.driver.find_elements_by_link_text('下一页'):
                self.next_page()
                links = self.write_links()


if __name__ == '__main__':
    s = Spider()
    s.query_page('数据', '南京')
    s.run()
