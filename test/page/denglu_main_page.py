from selenium.webdriver.common.by import By
from test.common.page import Page

class DendluMainPage(Page):
    loc_usname_input = (By.XPATH,'//*[@type="text"]')
    loc_password_input = (By.XPATH,'//*[@type="password"]')
    loc_denglu_button = (By.XPATH,'//*[@class="mint-button mint-button--default mint-button--large default usableBtn"]')


    def denglu(self,usname,password):
        '''登录功能'''
        self.logger("进入登录页面")
        self.find_element(*self.loc_usname_input).clear()
        self.find_element(*self.loc_usname_input).send_keys(usname)
        self.find_element(*self.loc_password_input).send_keys(password)
        self.find_element(*self.loc_denglu_button).click()
        self.wait()
        self.logger("正在登录中")