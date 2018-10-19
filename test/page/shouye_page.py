from selenium.webdriver.common.by import By
from test.common.page import Page
import time

class ShouyePage(Page):
    loc_search = (By.XPATH,'//*[@class="search"]')
    #未登录首页元素
    loc_name_span = (By.XPATH,'//span[@class="userName"]')
    #滑动元素定位
    loc_app_div = (By.XPATH,'//*[@id="app"]')
    #首页菜单
    loc_sycd_div = (By.XPATH,'//div[@class="wrapper-item"]')

    def dengluzhuangtai(self,user_name):
        if user_name in self.find_element(*self.loc_name_span).text:
            self.logger("登录成功")
            self.wait(1)
        else:
            self.logger("登录失败")
            # self.save_screen_shot("test_登录失败")
            raise AssertionError("登录失败，用户名未获取到")

    def search_jijin(self):
        self.logger("点击首页搜索文本框")
        self.find_element(*self.loc_search).click()
        self.wait()
        self.logger("跳转搜索基金页面中")

    def sycd(self):
        for i in range(len(self.find_elements(*self.loc_sycd_div))):
            cdname = self.find_elements(*self.loc_sycd_div)[i].text
            self.logger("切换首页" + cdname)
            self.find_elements(*self.loc_sycd_div)[i].click()
            title = self.page_title()
            self.wait()
            if i == 0:
                if "基金净值" in title:
                    self.logger("最新净值切换成功")
                    self.houtui()
                else:
                    raise AssertionError("首页菜单切换失败")
            elif title in cdname:
                self.logger("%s切换成功"%(title))
                self.houtui()
            else:
                self.logger("%s菜单切换失败"%(cdname))
                raise AssertionError("菜单切换失败")


