from selenium.webdriver.common.by import By
from test.common.page import Page


class JiaoYiJieGuo(Page):
    #业务类型
    loc_type_span = (By.XPATH,'//div[@class="type"]/span')
    #结果页面基金名称
    loc_fundname_span = (By.XPATH,'//*[@class="fundname"]')
    #结果页面支付银行卡名称
    loc_bankname_span = (By.XPATH,'//*[@class="bank"]/span')
    #数额
    loc_number_span = (By.XPATH,'//*[class="trade-amount"]/span')
    #申请已受理div元素
    loc_result_div = (By.XPATH,'//*[contains(text(),"申请已受理")]')
    #完成按钮
    loc_wancheng_button = (By.XPATH,'//*[@class="btn-warpper"]/button[1]')
    #查看详情按钮
    loc_xiangqing_button = (By.XPATH,'//button[@class="btn" and contains(text(),"查看详情")]')

    #获取页面基金名称
    def page_fundname(self,fundname):
        self.logger("获取页面基金名称")
        if self.find_element(*self.loc_fundname_span).text != fundname:
            self.logger("交易页面基金名称显示错误")
            # self.save_screen_shot("交易页面基金名称显示错误")
            raise AssertionError("交易结果页面基金名称与购买基金不一致")
        else:
            self.logger("交易页面基金名称显示正确")


    #获取页面交易类型
    def page_type(self):
        return self.find_element(*self.loc_type_span).text

    #获取结果页面的支付银行卡名称
    def page_bankname(self):
        return self.find_element(*self.loc_bankname_span).text

    #点击完成按钮
    def page_wancheng(self):
        self.logger("开始点击完成按钮")
        self.execute("arguments[0].click()",self.find_element(*self.loc_wancheng_button))
        #self.find_element(*self.loc_wancheng_button).click()
        self.logger("完成按钮点击完成")
        self.wait()