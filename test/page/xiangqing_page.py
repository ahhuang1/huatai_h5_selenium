from selenium.webdriver.common.by import By
from test.common.page import Page


class XingQing(Page):
    loc_fundcode_span = (By.XPATH,'//*[@class="fundcode"]')
    #可购买按钮
    loc_goumai_button = (By.XPATH,'//*[@class="fund-button red-button col-25"]')
    #可定投按钮
    loc_dintou_button = (By.XPATH, '//*[@class="fund-button button-border col-25" and contains(text(),"定投")]')
    #分享按钮
    loc_fenxiang_button = (By.XPATH, '//*[@class="fund-button button-border col-25" and contains(text(),"分享")]')
    #自选按钮
    loc_zixuan_button = (By.XPATH, '//*[@class="fund-button col-25" and contains(text(),"自选")]')


    #点击购买按钮
    def goumai(self):
        self.logger("点击购买按钮")
        self.find_element(*self.loc_goumai_button).click()
        self.wait()

    #点击定投按钮
    def dintou(self):
        self.logger("点击定投按钮")
        self.find_element(*self.loc_dintou_button).click()
        self.wait()

    #返回详情页面基金名称
    def fundcode(self,fund_code):
        if fund_code != self.find_element(*self.loc_fundcode_span).text:
            self.logger("基金code值与详情不一致")
            # self.save_screen_shot("基金code值与详情不一致")
            raise AssertionError("基金code值与详情不一致")
        else:
            self.logger("基金code值正确")