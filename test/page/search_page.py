from selenium.webdriver.common.by import By
from test.common.page import Page


class Search(Page):
    #搜索文本框
    loc_search_input = (By.XPATH,'//*[@type="text"]')
    #搜索结果列表
    loc_search_result = (By.XPATH,'//*[@class="fundItem"]')
    #转入按钮
    loc_zhuanru_span = (By.XPATH,'//span[contains(text(),"转入")]')
    #搜索基金并点击搜索结果
    def search_result(self,search_content):
        self.logger("进入搜索基金页面")
        self.execute('arguments[0].click',self.find_element(*self.loc_search_input))
        self.find_element(*self.loc_search_input).send_keys(search_content)
        self.logger("填写内容开始搜索")
        self.wait()
        self.find_elements(*self.loc_search_result)[0].click()
        self.logger("点击搜索结果第一项")
        self.wait(4)

    #搜索转入基金并点击转入按钮
    def search_zhxx(self,search_content):
        self.logger("搜索转入基金信息")
        self.execute('arguments[0].click', self.find_element(*self.loc_search_input))
        self.find_element(*self.loc_search_input).send_keys(search_content)
        self.logger("填写内容开始搜索")
        self.wait()
        self.find_element(*self.loc_zhuanru_span).click()
        self.wait(6)