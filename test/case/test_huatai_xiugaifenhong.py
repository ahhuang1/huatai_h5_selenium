import unittest
from config.config import login_url
from utils import read_excel
from config import config
from ddt import ddt,data
from test.common import browser
from test.page.denglu_main_page import DendluMainPage
from test.page.shouye_page import ShouyePage
from test.page.mine_page import Mine
from test.page.wodejijin_page import WoDeJiJin
from test.page.chicangxiangqing_page import ChiCangXiangQing
from test.page.xiugaifenhong_page import XiuGaiFenHong
from test.page.jiaoyijilu_page import JiaoYiJiLu
from test.page.jiaoyixiangqing_page import JiaoYiXiangQing


test = read_excel.ExcelUtil(config.DATA_PATH + '\\基金修改分红.xlsx', 'test').next()
url = login_url

@ddt
class xiugaifenhongTest(unittest.TestCase):
    '''修改基金分红方式测试'''
    @classmethod
    def setUpClass(self):
        self.page = DendluMainPage().get(url)

    @classmethod
    def tearDownClass(self):
        self.page.quit()

    def tearDown(self):
        self.page.refresh()
        self.page.get_newurl(url)
        self.page = DendluMainPage(self.page)
        self.page.wait(1)


    @data(*test)
    def test_xgfh(self, data):
        '''修改基金分红方式'''
        try:

            self.page.logger("登录-我的-持仓基金-修改分红-修改分红撤单")
            self.page.denglu(data['用户名'], data['密码'])
            self.page = ShouyePage(self.page)
            self.page.caidan("我的")
            self.page = Mine(self.page)
            self.page.djzc("基金产品")
            self.page = WoDeJiJin(self.page)
            self.page.djjjkp(data["基金代码"])
            self.page = ChiCangXiangQing(self.page)
            self.page.djxgfh()
            self.page = XiuGaiFenHong(self.page)
            fhfs = self.page.xgfh(data["交易密码"])
            self.page = ChiCangXiangQing(self.page)
            self.page.houtui()
            self.page = WoDeJiJin(self.page)
            self.page.houtui()
            self.page = Mine(self.page)
            self.page.djcd("撤单")
            self.page = JiaoYiJiLu(self.page)
            self.page.chakanxiangqing(0)
            self.page = JiaoYiXiangQing(self.page)
            xqfhfs = self.page.hqfhfs()
            if xqfhfs in fhfs:
                self.page.logger("交易记录显示修改方式正确")
            else:
                self.page.logger("修改分红方式错误%s"%(xqfhfs))
                self.page.save_screen_shot("test_修改分红")
                self.imgs.append(self.page.driver.get_screenshot_as_base64())
                raise AssertionError("修改分红方式错误")
            self.page.chedan(data["交易密码"])
            self.page.logger("修改分红方式成功")
        except:
            self.page.logger("修改分红方式测试失败")
            self.page.save_screen_shot("test_修改分红")
            self.imgs.append(self.page.driver.get_screenshot_as_base64())
            raise AssertionError("修改分红方式失败")


if __name__ == '__main__':
    unittest.main()