import unittest
from config.config import login_url
from utils import read_excel
from config import config
from ddt import ddt,data
from test.page.denglu_main_page import DendluMainPage
from test.page.shouye_page import ShouyePage
from test.page.search_page import Search
from test.page.xiangqing_page import XingQing
from test.page.dingtou_page import DingTou
from test.page.mine_page import Mine
from test.page.wodedingtou_page import WoDeDingTou
from test.page.dingtoumingxi_page import DingTouMingXi


test = read_excel.ExcelUtil(config.DATA_PATH + '\\基金定投.xlsx', 'test').next()
url = login_url

@ddt
class dingtouTest(unittest.TestCase):
    '''基金定投流程测试'''
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
    def test_jjdt(self,data):
        '''定投基金-修改-暂停-终止'''
        try:
            self.page.logger("登录-搜索基金-定投基金-完成-我的-我的定投-修改-暂停-终止")
            self.page.denglu(data['用户名'], data['密码'])
            self.page = ShouyePage(self.page)
            self.page.dengluzhuangtai(data['用户姓'])
            self.page.search_jijin()
            self.page = Search(self.page)
            self.page.search_result(data['搜索基金代码'])
            self.page = XingQing(self.page)
            self.page.fundcode(data['基金代码'])
            self.page.dintou()
            self.page = DingTou(self.page)
            self.page.bj_code(data['基金代码'])
            self.page.xzdt(data["付款方式"],data['定投金额'],data['交易密码'],data["定投周期"],data["定投日期"])
            self.page.logger("返回搜索基金页面")
            self.page.houtui()
            self.page.logger("返回首页")
            self.page.houtui()
            self.page.caidan("我的")
            self.page = Mine(self.page)
            self.page.djcd("我的定投")
            self.page = WoDeDingTou(self.page)
            self.page.dtjc(data["基金名称"],data['基金代码'],data['付款方式'],data["定投金额"],data["定投周期"],data["定投日期"])
            self.page.dtck()
            self.page = DingTouMingXi(self.page)
            self.page.dtmxjc(data["基金名称"], data['基金代码'], data['付款方式'], data["定投金额"], data["定投周期"], data["定投日期"])
            self.page.dtxg()
            self.page = DingTou(self.page)
            self.page.xzdt(data["付款方式"],data['修改定投金额'],data['交易密码'],data["修改定投周期"],data["修改定投日期"],sfxg=False)
            self.page = WoDeDingTou(self.page)
            self.page.dtjc(data["基金名称"], data['基金代码'], data['付款方式'], data["修改定投金额"], data["修改定投周期"], data["修改定投日期"])
            self.page.wait()
            self.page.dtck()
            self.page = DingTouMingXi(self.page)
            self.page.dtzt(data["交易密码"])
            self.page = WoDeDingTou(self.page)
            self.page.dtztjc()
            num = self.page.kpzs()
            self.page.dtzzck()
            self.page = DingTouMingXi(self.page)
            self.page.dtzz(data["交易密码"])
            self.page = WoDeDingTou(self.page)
            num2 = self.page.kpzs()
            if num - num2 == 1:
                self.page.logger("终止定投成功")
            else:
                self.page.logger("终止定投失败")
                raise AssertionError("终止定投失败")

        except:
            self.page.logger("定投流程测试失败")
            self.page.save_screen_shot("test_定投")  # 用来保存截图报本地
            self.imgs.append(self.page.driver.get_screenshot_as_base64())
            raise AssertionError("定投流程测试失败")

if __name__ == '__main__':
    unittest.main()
