from selenium.webdriver.common.by import By
from test.common.page import Page

class MaiJiJinFangShi(Page):
    #卖基金方式:
    loc_mjjfs_div = (By.XPATH,'//div[@class="channel-list"]/div')
    # 普通取现和快速取现
    loc_qx_div = (By.XPATH, '//div[@class="cashout-type"]')

    #选择赎回方式
    def xzshfs(self,shfs):
        self.logger("选择%s" % (shfs))
        if shfs == "普通取现":
            self.find_elements(*self.loc_qx_div)[0].click()
        if shfs == "快速取现":
            self.find_elements(*self.loc_qx_div)[1].click()
        if shfs == "现金宝":
            self.find_elements(*self.loc_mjjfs_div)[0].click()
        if shfs == "银行卡":
            self.find_elements(*self.loc_mjjfs_div)[1].click()
        if shfs == "基金转换":
            self.find_elements(*self.loc_mjjfs_div)[2].click()
        self.wait()

