from selenium.webdriver.common.by import By
from test.common.page import Page

class XiuGaiFenHong(Page):
    #分红方式
    loc_fhfs_div = (By.XPATH,'//div[@class="divide-type"]')
    #确认修改按钮
    loc_qrxg_button = (By.XPATH,'//button[@class="btn"]')

    #修改分红方式
    def xgfh(self,password):
        self.logger("修改分红方式")
        fhfs = self.find_elements(*self.loc_fhfs_div)[1].text
        self.find_elements(*self.loc_fhfs_div)[1].click()
        self.wait()
        self.find_element(*self.loc_qrxg_button).click()
        self.mmqd(password)
        return fhfs

