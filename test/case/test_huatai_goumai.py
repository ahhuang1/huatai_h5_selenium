import unittest
from config.config import login_url
from utils import read_excel
from config import config
from ddt import ddt,data
from test.page.denglu_main_page import DendluMainPage
from test.page.shouye_page import ShouyePage
from test.page.search_page import Search
from test.page.xiangqing_page import XingQing
from test.page.jiaoyi_page import JiaoYi
from test.page.jiaoyijieguo_page import JiaoYiJieGuo
from test.page.mine_page import Mine
from test.page.jiaoyijilu_page import JiaoYiJiLu
from test.page.jiaoyixiangqing_page import JiaoYiXiangQing

test = read_excel.ExcelUtil(config.DATA_PATH + '\\基金购买.xlsx', 'test').next()
url = login_url

@ddt
class goumaiTest(unittest.TestCase):
    '''基金购买流程测试'''
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
        self.page.wait()

    @data(*test)
    def test_jjgm(self,data):
        '''登录-购买基金-撤单'''
        try:
            self.page.logger("登录-搜索基金-购买基金-完成按钮-我的-交易记录-可撤单详情-撤单")
            self.page.denglu(data['用户名'], data['密码'])
            self.page = ShouyePage(self.page)
            self.page.dengluzhuangtai(data['用户姓'])
            self.page.search_jijin()
            self.page = Search(self.page)
            self.page.search_result(data['搜索基金代码'])
            self.page = XingQing(self.page)
            self.page.fundcode(data['基金代码'])
            self.page.goumai()
            self.page = JiaoYi(self.page)
            self.page.goumai(data["付款方式"],data['购买金额'],data['交易密码'])
            self.page = JiaoYiJieGuo(self.page)
            self.page.page_fundname(data["基金名称"])
            self.page.page_wancheng()
            self.page.logger("现金宝购买基金流程成功")
            self.page = Mine(self.page)
            self.page.jiaoyijilu()
            self.page = JiaoYiJiLu(self.page)
            self.page.qh_tab("可撤单")
            self.page.chakanxiangqing(0)
            self.page = JiaoYiXiangQing(self.page)
            self.page.title()
            self.page.chedan(data['交易密码'])
            self.page.logger("购买流程用例执行通过")
        except:
            self.page.logger("购买流程测试失败")
            self.page.save_screen_shot("test_购买")
            self.imgs.append(self.page.driver.get_screenshot_as_base64())
            raise AssertionError("购买流程失败")


if __name__ == '__main__':
    unittest.main()