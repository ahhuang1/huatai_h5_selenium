from selenium.webdriver.common.by import By
from test.common.page import Page

class MaiJiJin(Page):
    #基金卡片
    loc_mjjlb_div = (By.XPATH,'//div[@class="sell-fund-item"]')
    #卖出按钮
    loc_mc_button = (By.XPATH,'//button[@class="sellBtn last"]')
    #可用余额
    loc_kyye_span = (By.XPATH,'//span[@class="share"]')

    #取出卖出基金卡片信息
    def hqxx(self):
        list_len = len(self.find_elements(*self.loc_mjjlb_div))
        list_mjj = []
        for i in range(list_len):
            list_mjj.append(self.find_elements(*self.loc_mjjlb_div)[i].text)
        return list_mjj

    #选择卖出基金并返回卖出基金的可用份额
    def xzmjj(self,bank,fundcode):
        list_mjj = self.hqxx()
        hdxx = [bank,fundcode]
        hang = None

        #获取卖基金的行数
        for i in list_mjj:
            if all(t in i for t in hdxx):
                hang = list_mjj.index(i)
            else:
                pass
        if hang > 4:
            self.huadong()
        kyye = self.find_elements(*self.loc_kyye_span)[hang].text
        self.find_elements(*self.loc_mc_button)[hang].click()
        self.wait()
        return kyye



