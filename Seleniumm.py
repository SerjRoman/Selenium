from selenium import webdriver
driver = webdriver.Chrome() 
class Wikipedia():
    def __init__(self,driver,www,xpath1,xpath2):
        self.driver = driver
        self.www = www
        self.xpath1 = xpath1
        self.xpath2 = xpath2
    def Title(self):
        title_elem=driver.get(self.www)
        title_elem=driver.find_element_by_xpath(self.xpath1)
        print(title_elem.text)
    def H1_elem(self):
        H2_elem=driver.get(self.www)
        H2_elem=driver.find_element_by_xpath(self.xpath2)
        print(H2_elem.text)
Theatre=Wikipedia(driver,'https://ru.wikipedia.org/wiki/%D0%A2%D0%B5%D0%B0%D1%82%D1%80_(%D0%B0%D1%80%D1%85%D0%B8%D1%82%D0%B5%D0%BA%D1%82%D1%83%D1%80%D0%BD%D0%BE%D0%B5_%D1%81%D0%BE%D0%BE%D1%80%D1%83%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5)#%D0%A3%D1%81%D1%82%D1%80%D0%BE%D0%B9%D1%81%D1%82%D0%B2%D0%BE','//h1','//h3[1]')
Theatre.Title()
Theatre.H1_elem()
print('Hello World!!!')
