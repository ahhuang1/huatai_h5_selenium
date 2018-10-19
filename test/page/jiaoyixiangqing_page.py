from selenium.webdriver.common.by import By
from test.common.page import Page

class JiaoYiXiangQing(Page):
    #标题
    loc_title_h1 = (By.XPATH,'//h1[@class="mint-header-title"]')
    #撤单按钮
    loc_cd_button = (By.XPATH,'//button[contains(text(),"撤单")]')
    #撤单详情元素
    loc_cdjg_div = (By.XPATH,'//div[contains(@class,"fund-android")]')
    # 密码输入框
    loc_jiaoyimima_input = (By.XPATH, '//*[@type="password"]')
    # 交易确定框
    loc_queding_button = (By.XPATH, '//*[@class="message-box-btn confirm-btn"]')
    #分红方式
    loc_xgfhfs_sapn = (By.XPATH,'//div[@class="bank"]/span[1]')
    #获取交易详情标题
    def title(self):
        self.logger("查看交易标题")
        if self.find_element(*self.loc_title_h1).text == "交易详情":
            self.logger("成功切换至交易详情页面")
        else:
            self.logger("页面切换错误。改页面标题为：%s"%(self.find_element(*self.loc_title_h1).text))
            # self.save_screen_shot("test_标题错误")
            raise AssertionError("切换至交易详情页面失败")

    def chedan(self,password):
        try:
            self.logger("进入撤单流程")
            self.logger("点击撤单按钮")
            self.find_element(*self.loc_cd_button).click()
            self.wait(1)
            self.logger("输入交易密码")
            self.find_element(*self.loc_jiaoyimima_input).send_keys(password)
            self.logger("点击确定按钮")
            self.find_element(*self.loc_queding_button).click()
            self.wait(6)
            if "交易已撤单" in self.find_element(*self.loc_cdjg_div).text:
                self.logger("撤单成功")
            else:
                self.logger("撤单失败")
                # self.save_screen_shot("test_撤单失败")
                raise AssertionError("撤单流程失败")
        except:
            self.logger("撤单流程失败")
            # self.save_screen_shot("test_撤单失败")
            raise AssertionError("撤单流程失败")

    def hqfhfs(self):
        text = self.find_element(*self.loc_xgfhfs_sapn).text
        return text[3:]
