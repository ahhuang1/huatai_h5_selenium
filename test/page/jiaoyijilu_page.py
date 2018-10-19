from selenium.webdriver.common.by import By
from test.common.page import Page


class JiaoYiJiLu(Page):
    #被选中tab元素
    loc_xztab_div = (By.XPATH,'//div[contains(@class,"tab-item-focus")]')
    #待确认tab
    loc_dqr_div = (By.XPATH,'//div[@class="record"]/div[1]/div[1]')
    #历史交易tab
    loc_lsjy_div = (By.XPATH,'//div[@class="record"]/div[1]/div[2]')
    #可撤单tab
    loc_kcd_div = (By.XPATH,'//div[@class="record"]/div[1]/div[3]')
    #分红记录tab
    loc_fhjl_div = (By.XPATH,'//div[@class="record"]/div[1]/div[4]')
    #待确认列表-可撤单-分红记录
    loc_lb_div = (By.XPATH,'//div[@class="record-item"]')
    #历史交易列表
    loc_lsjy_div = (By.XPATH, '//div[@class="confrim-rec-item"]')

    #切换交易记录tab
    def qh_tab(self,text):
        self.logger("切换至"+ text)
        if text == "待确认":
            self.find_element(*self.loc_dqr_div).click()
            self.wait()
            if self.find_element(*self.loc_xztab_div).text == text:
                self.logger("成功切换至" + text)
            else:
                self.logger("切换失败")
                # self.save_screen_shot("test_切换失败")
                raise AssertionError("切换失败")
        if text == "历史记录":
            self.find_element(*self.loc_lsjy_div).click()
            self.wait()
            if self.find_element(*self.loc_xztab_div).text == text:
                self.logger("成功切换至"+ text)
            else:
                self.logger("切换失败")
                # self.save_screen_shot("test_切换失败")
                raise AssertionError("切换失败")
        if text == "可撤单":
            self.find_element(*self.loc_kcd_div).click()
            self.wait()
            if str(self.find_element(*self.loc_xztab_div).text) == text:
                self.logger("成功切换至"+ text)
            else:
                self.logger("切换失败")
                # self.save_screen_shot("test_切换失败")
                raise AssertionError("切换失败")
        if text == "分红记录":
            self.find_element(*self.loc_fhjl_div).click()
            self.wait()
            if self.find_element(*self.loc_xztab_div).text == text:
                self.logger("成功切换至"+ text)
            else:
                self.logger("切换失败")
                # self.save_screen_shot("test_切换失败")
                raise AssertionError("切换失败")

    #查看交易记录tab详情
    def chakanxiangqing(self,num):
        self.logger("查看tab列表下第%s条记录"%(num))
        if self.find_elements(*self.loc_lb_div):
            self.find_elements(*self.loc_lb_div)[num].click()
        else:
            self.logger("该交易记录tab下无记录")
            # self.save_screen_shot("test_切换失败")
            raise AssertionError("该交易记录tab下无记录")
        self.wait()
        self.logger("进入交易记录详情")


    def jianchajiaoyi(self,num):
        self.logger("检查查看交易记录")
        if "实时确认成功" in self.find_elements(*self.loc_lb_div)[num].text:
            self.logger("快速赎回确认成功")
        else:
            self.logger("该交易记录tab下无记录")
            # self.save_screen_shot("test_切换失败")
            raise AssertionError("该交易记录tab下无记录")
        self.wait(1)

