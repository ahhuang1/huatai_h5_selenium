from selenium.webdriver.common.by import By
from test.common.page import Page

class XJBZiChan(Page):
    #现金宝总资产
    loc_xjbzzc_div = (By.XPATH,'//div[contains(text(),"现金宝资产")]/../div[2]')
    #现金宝可用余额
    loc_xjbky_div = (By.XPATH,'//span[contains(text(),"可用余额")]/../span[2]')
    #下列按钮
    loc_button_div = (By.XPATH,'//div[@class="fixed-navbar"]/div')

    #现金宝资产
    def xjbzc(self):
        xjbzzc = self.find_element(*self.loc_xjbzzc_div).text
        xjbky = self.find_element(*self.loc_xjbky_div).text
        return xjbzzc,xjbky

    def dj_xjbbutton(self,caidan):
        self.logger("点击现金宝%s按钮"%(caidan))
        if caidan == "充值":
            self.find_elements(*self.loc_button_div)[0].click()
            self.logger("进入现金宝充值页面")
        if caidan == "取现":
            self.find_elements(*self.loc_button_div)[1].click()
            self.logger("进入现金宝取现页面")
        if caidan == "买基金":
            self.find_elements(*self.loc_button_div)[2].click()
            self.logger("进入现金宝买基金页面")
        self.wait()


