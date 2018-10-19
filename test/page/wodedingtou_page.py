from selenium.webdriver.common.by import By
from test.common.page import Page

class WoDeDingTou(Page):
    #定投卡片
    loc_dtkp_div = (By.XPATH,'//div[@class="my-plan-item"][1]')
    #新增定投按钮
    loc_xzdt_button = (By.XPATH,'//span[contains(text(),"新增定投")]')
    #定投卡片总数
    loc_zdtkp_div = (By.XPATH,'//div[@class="my-plan-item"]')

    #求出定投计划总数
    def kpzs(self):
        num = len(self.find_elements(*self.loc_zdtkp_div))
        return num

    def dtjc(self,fundname,fundcode,fkfs,dtje,dtzj,dtrq):
        self.logger("检查我的定投卡片信息")
        list = [fundname,fundcode,fkfs,dtje,dtzj,dtrq]
        list1 = [fundname,fundcode,dtje,dtzj,dtrq]
        text = self.find_element(*self.loc_dtkp_div).text
        if fkfs != "银行卡":
            if all(t in text for t in list):
                self.logger("定投基金卡片信息准确")
            else:
                # self.save_screen_shot("test_定投信息失败")
                raise AssertionError("定投基金卡片信息错误")
        elif fkfs == "银行卡":
            if ("现金宝" not in text) and ("其它货币" not in text):
                if all(t in text for t in list1):
                    self.logger("定投基金卡片信息准确")
                else:
                    # self.save_screen_shot("test_定投信息失败")
                    raise AssertionError("定投基金卡片信息错误")
            else:
                # self.save_screen_shot("test_定投信息失败")
                raise AssertionError("定投基金卡片信息错误")
    #定投查看
    def dtck(self):
        self.logger("点击定投基金卡片")
        self.find_element(*self.loc_dtkp_div).click()
        self.wait()

    def dtzzck(self):
        self.logger("点击暂停的定投基金卡片")
        if self.kpzs() >= 4:
            self.huadong()
        self.find_elements(*self.loc_zdtkp_div)[-1].click()
        self.wait()

    #暂停定投检查
    def dtztjc(self):
        self.logger("检查定投状态")
        text = self.find_elements(*self.loc_zdtkp_div)[-1].text
        if "暂停" in text:
            self.logger("定投计划成功暂停")
        else:
            # self.save_screen_shot("定投计划暂停失败")
            raise AssertionError("定投计划暂停失败")

