from selenium.webdriver.common.by import By
from test.common.page import Page

class KeZhuanHuan(Page):
    #基金卡片
    loc_kzhlb_div = (By.XPATH,'//div[@class="convert-fund-item"]')
    #转出按钮
    test = "转出"
    loc_mc_button = (By.XPATH,'//span[contains(text(),"转出")]')
    #可用余额
    loc_kyye_span = (By.XPATH,'//div[@class="use-share"]/span[1]')

    #取出可转换基金卡片信息
    def hqzhxx(self):
        list_len = len(self.find_elements(*self.loc_kzhlb_div))
        list_kzh = []
        for i in range(list_len):
            list_kzh.append(self.find_elements(*self.loc_kzhlb_div)[i].text)
        return list_kzh

    #选择卖出基金并返回卖出基金的可用份额
    def xzmjj(self,bank,fundcode):
        list_mjj = self.hqzhxx()
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