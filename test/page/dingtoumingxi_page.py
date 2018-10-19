from selenium.webdriver.common.by import By
from test.common.page import Page

class DingTouMingXi(Page):
    #定投明细
    loc_dtmx_div = (By.XPATH,'//div[@class="my-plan-detail"]')
    #修改按钮
    loc_dtxg_div = (By.XPATH,'//div[contains(text(),"修改")]')
    # 暂停按钮
    loc_dtzt_div = (By.XPATH, '//div[@class="my-plan-bottom-bar row"]/div[2]')
    # 终止按钮
    loc_dtzz_div = (By.XPATH, '//div[contains(text(),"终止")]')
    # 密码输入框


    def dtmxjc(self, fundname, fundcode, fkfs, dtje, dtzj, dtrq):
        self.logger("检查我的定投卡片信息")
        list = [fundname,fundcode,fkfs,dtje,dtzj,dtrq]
        list1 = [fundname,fundcode,dtje,dtzj,dtrq]

        text = self.find_element(*self.loc_dtmx_div).text

        if fkfs != "银行卡":

            if all(t in text for t in list):
                self.logger("定投基金卡片信息准确")
            else:
                raise AssertionError("定投基金卡片信息错误")
        elif fkfs == "银行卡":
            if ("现金宝" not in text) and ("其它货币" not in text):
                if all(t in text for t in list1):
                    self.logger("定投基金卡片信息准确")
                else:
                    raise AssertionError("定投基金卡片信息错误")
            else:
                raise AssertionError("定投基金卡片信息错误")

    def dtxg(self):
        self.logger("点击修改按钮")
        self.find_element(*self.loc_dtxg_div).click()
        self.wait()

    def dtzt(self,password):
        self.logger("点击暂停按钮")
        self.find_element(*self.loc_dtzt_div).click()
        self.wait()
        self.mmqd(password)
        self.houtui()

    def dtzz(self,password):
        self.logger("点击终止按钮")
        self.find_element(*self.loc_dtzz_div).click()
        self.wait()
        self.mmqd(password)

