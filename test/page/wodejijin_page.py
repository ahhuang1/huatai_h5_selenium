from selenium.webdriver.common.by import By
from test.common.page import Page

class WoDeJiJin(Page):
    #基金卡片
    loc_wdjjkp_div = (By.XPATH,'//div[@class="fund-card mt-20"]')

    # 取出可转换基金卡片信息
    def hqjjxx(self):
        list_len = len(self.find_elements(*self.loc_wdjjkp_div))
        list_jjxx = []
        for i in range(list_len):
            list_jjxx.append(self.find_elements(*self.loc_wdjjkp_div)[i].text)
        return list_jjxx

    # 点击基金卡片
    def djjjkp(self, fundcode):
        list_kpxx = self.hqjjxx()
        hdxx = [fundcode]
        hang = None
        # 获取基金卡片的行数
        for i in list_kpxx:
            if all(t in i for t in hdxx):
                hang = list_kpxx.index(i)
            else:
                pass
        if hang > 2:
            self.huadong()
        self.find_elements(*self.loc_wdjjkp_div)[hang].click()
        self.wait()