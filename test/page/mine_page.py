from selenium.webdriver.common.by import By
from test.common.page import Page


class Mine(Page):
    #交易记录按钮
    loc_jiaoyijilu_laber = (By.XPATH,'//button[@class="mint-button trade-history mint-button--default mint-button--normal"]')
    #快捷菜单栏按钮
    loc_qhcd_span = (By.XPATH,'//div[@class="point-box"]/span[2]')
    #[买基金，卖基金，充值，取现，银行卡，我的定投，基金转换，分红方式，撤单，搜索]
    loc_caidan_div = (By.XPATH,'//div[@class="option-box"]/div/div')
    #我的定投
    loc_wddt_div = (By.XPATH,'//div[contains(text(),"我的定投")]')
    #风险等级按钮
    loc_fengxiandengji_div = (By.XPATH,'//*[@class="value tui-flex-1 t-right"]')
    #总资产
    loc_zongzichan_span = (By.XPATH,'//span[@class="num fund-android"]')
    #现金宝
    loc_xjb_div = (By.XPATH,'//div[@class="t-cell-title" and contains(text(),"现金宝")]')
    #基金产品
    loc_jjcp_div = (By.XPATH,'//div[@class="t-cell-title" and contains(text(),"基金产品")]')
    #资产
    loc_zc_span = (By.XPATH,'//span[@class="cell-title fund-android"]')

    #查看交易记录
    def jiaoyijilu(self):
        self.logger("进入交易记录")
        self.find_element(*self.loc_jiaoyijilu_laber).click()
        self.wait()

    #切换快捷菜单至第二行
    def qhkjcd(self):
        self.logger("切换快捷菜单到第二行")
        self.find_element(*self.loc_qhcd_span).click()
        self.wait(2)

    #选择快捷菜单
    def djcd(self,kjcdm):
        self.logger("点击快捷菜单")
        if kjcdm == "买基金":
            self.find_elements(*self.loc_caidan_div)[0].click()
        if kjcdm == "卖基金":
            self.find_elements(*self.loc_caidan_div)[1].click()
        if kjcdm == "充值":
            self.find_elements(*self.loc_caidan_div)[2].click()
        if kjcdm == "取现":
            self.find_elements(*self.loc_caidan_div)[3].click()
        if kjcdm == "银行卡":
            self.find_elements(*self.loc_caidan_div)[4].click()
        if kjcdm == "我的定投":
            self.execute("arguments[0].click()",self.find_elements(*self.loc_caidan_div)[5])
        if kjcdm == "基金转换":
            ys = self.find_elements(*self.loc_caidan_div)[6]
            self.qhkjcd()
            ys.click()
        if kjcdm == "分红方式":
            ys = self.find_elements(*self.loc_caidan_div)[7]
            self.qhkjcd()
            ys.click()
        if kjcdm == "撤单":
            ys = self.find_elements(*self.loc_caidan_div)[8]
            self.qhkjcd()
            ys.click()
        if kjcdm == "搜索":
            ys = self.find_elements(*self.loc_caidan_div)[9]
            self.qhkjcd()
            ys.click()
        self.wait(4)

    #点击资产
    def djzc(self,zichan):
        if zichan == "现金宝":
            zc = self.find_elements(*self.loc_zc_span)[0].text
            if float(zc) > 0:
                self.logger("现金宝资产为%s"%zc)
                self.find_elements(*self.loc_zc_span)[0].click()
            else:
                self.logger("现金宝资产获取异常")
                # self.save_screen_shot("test_我的页面加载失败")
                raise AssertionError("我的页面加载错误")
        if zichan == "基金产品":
            zc = self.find_elements(*self.loc_zc_span)[1].text
            if float(zc) > 0:
                self.logger("基金产品资产为%s"%zc)
                self.find_elements(*self.loc_zc_span)[1].click()
            else:
                self.logger("基金产品资产获取异常")
                # self.save_screen_shot("test_我的页面加载失败")
                raise AssertionError("我的页面加载错误")
        self.wait(4)
        return zc
