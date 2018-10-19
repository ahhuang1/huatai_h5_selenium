from selenium.webdriver.common.by import By
from test.common.page import Page

class QXXiangQing(Page):
    #赎回输入框
    loc_shuhui_input = (By.XPATH,'//input[@type="number"]')
    #取现按钮
    loc_qx_button = (By.XPATH,'//button[contains(text(),"取现")]')
    #卖出按钮
    loc_mc_button = (By.XPATH, '//button[contains(text(),"卖出")]')
    #转换按钮
    loc_zh_button = (By.XPATH, '//button[contains(text(),"转换")]')


    def kemaichuzc(self):
        txzc = self.find_element(*self.loc_shuhui_input).get_attribute("placeholder")
        self.logger(txzc)
        return txzc

    #现金宝取现
    def djqx(self,qxje,password):
        self.find_element(*self.loc_shuhui_input).send_keys(qxje)
        self.logger("点击取现按钮")
        self.wait(2)
        self.find_element(*self.loc_qx_button).click()
        self.mmqd(password)

    #基金卖出回现金宝或银行卡
    def djmc(self,mcje,password):
        self.find_element(*self.loc_shuhui_input).send_keys(mcje)
        self.logger("点击卖出按钮")
        self.wait(2)
        self.find_element(*self.loc_mc_button).click()
        self.mmqd(password)

    #点击转换按钮
    def djzh(self,zhfe,password):
        self.find_element(*self.loc_shuhui_input).send_keys(zhfe)
        self.logger("点击转换按钮")
        self.wait(2)
        self.find_element(*self.loc_zh_button).click()
        self.mmqd(password)