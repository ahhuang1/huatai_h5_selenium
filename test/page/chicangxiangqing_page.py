from selenium.webdriver.common.by import By
from test.common.page import Page

class ChiCangXiangQing(Page):
    #修改分红按钮
    loc_xgfh_div = (By.XPATH,'//div[contains(text(),"修改分红")]')

    #点击修改分红按钮
    def djxgfh(self):
        #点击修改分红按钮
        self.find_element(*self.loc_xgfh_div).click()
