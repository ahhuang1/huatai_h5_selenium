from selenium.webdriver.common.by import By
from test.common.page import Page
import time

class JiaoYi(Page):
    #额度输入框
    loc_number_input = (By.XPATH,'//input[@type="number"]')
    #买入确定按钮
    loc_submit_button = (By.XPATH,'//button[@type="button"]')

    def goumai(self,bank,number,password):
        '''购买'''
        try:
            self.logger("现金宝购买基金中")
            self.xzfk(bank)
            self.find_element(*self.loc_number_input).send_keys(str(number))
            #self.wait(6)
            self.find_element(*self.loc_submit_button).click()
            self.mmqd(password)
            self.logger("提交现金宝购买交易")
        except:
            self.logger("现金宝购买基金失败")
            # self.save_screen_shot("test_交易页面")
            raise AssertionError("购买交易页面出错")
