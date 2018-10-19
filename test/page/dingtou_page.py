from selenium.webdriver.common.by import By
from test.common.page import Page

class DingTou(Page):
    #定投基金代码
    loc_fundcode_span = (By.XPATH,'//span[@class="fundcode"]')
    #定投周期
    loc_zhouqi_div = (By.XPATH,'//div[@class="plan-item-title" and contains(text(),"定投周期")]')
    #定投日期
    loc_riqi_div = (By.XPATH, '//div[@class="plan-item-title" and contains(text(),"定投日期")]')
    #付款方式
    loc_fangshi_div = (By.XPATH, '//div[@class="plan-item-title" and contains(text(),"付款方式")]')
    #定投金额
    loc_number_input = (By.XPATH,'//input[@type="number"]')
    #勾选框
    loc_checkbox_div = (By.XPATH,'//div[@class="read-rule"]/div')
    #确定按钮
    loc_queding_button = (By.XPATH,'//button[contains(text(),"确定")]')
    #周期选择（多元素）
    loc_xzzq_div = (By.XPATH,'//div[@class="fix-handle-box"]/div')
    #日期选择(多元素)
    loc_xzrq_div = (By.XPATH,'//div[@class="fix-head"]/../div[2]/div')
    #密码输入框
    loc_mima_div = (By.XPATH,'//input[@type="password"]')
    #密码确定按钮
    loc_mmqd_button = (By.XPATH,'//div[@class="message-box-btns-wrapper"]/button[contains(text(),"确定")]')
    #支付方式标题
    loc_zflb_div = (By.XPATH,'//div[@class="header"]/../div[2]/div')
    #现金宝支付方式第一个银行卡元素
    loc_xzb_div = (By.XPATH,'//div[@class="xjb-item"]')
    #现金宝银行卡列表
    loc_huobibanklists_div = (By.XPATH, '//*[@class="bankitem"]')

    #比较code
    def bj_code(self,fundcode):
        if fundcode == self.find_element(*self.loc_fundcode_span).text:
            self.logger("基金代码与定投基金一致")
        else:
            self.logger("基金代码与定投基金不一致")
            raise AttributeError("基金代码与选择定投基金不一致")

    #新增定投(修改定投)
    def xzdt(self,bank,jine,password,zhouqi,riqi,sfxg=True):
        try:
            if sfxg:
                self.logger("开始新增定投")
            if not sfxg:
                self.logger("开始修改定投")
            self.logger("选择定投周期")
            self.wait(3)
            self.execute("arguments[0].click()",self.find_element(*self.loc_zhouqi_div))
            #self.find_element(*self.loc_zhouqi_div).click()
            self.wait(1)
            if zhouqi == "每周" or zhouqi == "每两周" or zhouqi == "每月":
                if zhouqi == "每周":
                    self.find_elements(*self.loc_xzzq_div)[0].click()
                elif zhouqi == "每两周":
                    self.find_elements(*self.loc_xzzq_div)[1].click()
                elif zhouqi == "每月":
                    self.find_elements(*self.loc_xzzq_div)[2].click()
            else:
                self.logger("不支持%s定投周期"%(zhouqi))
            self.logger("选择定投日期")
            self.wait(3)
            self.execute("arguments[0].click()", self.find_element(*self.loc_riqi_div))
            #self.find_element(*self.loc_riqi_div).click()
            self.wait(2)
            if riqi:
                if riqi == "星期一":
                    self.find_elements(*self.loc_xzrq_div)[0].click()
                elif riqi == "星期二":
                    self.find_elements(*self.loc_xzrq_div)[1].click()
                elif riqi == "星期三":
                    self.find_elements(*self.loc_xzrq_div)[2].click()
                elif riqi == "星期四":
                    self.find_elements(*self.loc_xzrq_div)[3].click()
                elif riqi == "星期五":
                    self.find_elements(*self.loc_xzrq_div)[4].click()
                elif riqi:
                    self.find_elements(*self.loc_xzrq_div)[int(riqi)-1].click()
            else:
                self.logger("定投日期不能为空")
            self.logger("输入金额")
            self.execute("arguments[0].click()",self.find_element(*self.loc_number_input))
            self.wait(2)
            self.find_element(*self.loc_number_input).clear()
            self.find_element(*self.loc_number_input).send_keys(jine)
            self.logger("选择付款方式")
            self.wait(1)
            #判断是否新增还是修改
            if sfxg:
                self.find_element(*self.loc_fangshi_div).click()
                self.xzfk(bank)
            self.logger("勾选协议")
            self.wait(1)
            self.find_element(*self.loc_checkbox_div).click()
            self.logger("点击确定按钮")
            self.wait(1)
            self.find_element(*self.loc_queding_button).click()
            self.wait(1)
            self.logger("输入交易密码")
            self.find_element(*self.loc_mima_div).send_keys(password)
            self.wait(1)
            self.find_elements(*self.loc_mmqd_button)[0].click()
            if sfxg:
                self.logger("新增定投成功")
            if not sfxg:
                self.logger("修改定投成功")
            self.wait(4)
        except:
            self.logger("新增或修改定投失败")
            self.save_screen_shot("test_定投")
            raise AssertionError("新增或修改定投失败")








