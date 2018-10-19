from selenium.webdriver.common.by import By
from test.common.page import Page

class ZhangHaoGuanLi(Page):
    #账号管理页面各tab
    loc_zhcd_div = (By.XPATH,'//div[@class="title"]')
    #安全退出按钮
    loc_tuichu_button = (By.XPATH,'//div[@class="action-btn-group btn-wrapper"]')

    #选择账号管理页面菜单
    def xzzhxx(self,caidan):
        self.logger("选择账号管理页面第%s菜单"%(caidan))
        self.find_elements(*self.loc_zhcd_div)[caidan-1].click()
        self.wait()

    #退出当前账号
    def tuichu(self):
        self.logger("退出当前账号")
        self.find_element(*self.loc_tuichu_button).click()
        self.wait()

