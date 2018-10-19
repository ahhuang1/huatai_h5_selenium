import unittest
from config.config import login_url
from utils import read_excel
from config import config
from ddt import ddt,data
from test.common import browser
from test.page.denglu_main_page import DendluMainPage
from test.page.shouye_page import ShouyePage
from test.page.mine_page import Mine
from test.page.maijijin_page import MaiJiJin
from test.page.maijijinfangshi_page import MaiJiJinFangShi
from test.page.qxxiangqing_page import QXXiangQing
from test.page.jiaoyijilu_page import JiaoYiJiLu
from test.page.jiaoyixiangqing_page import JiaoYiXiangQing
from test.page.jiaoyijieguo_page import JiaoYiJieGuo
from test.page.search_page import Search

test = read_excel.ExcelUtil(config.DATA_PATH + '\\基金赎回.xlsx', 'test').next()
url = login_url

@ddt
class JJShuHui(unittest.TestCase):
    '''基金赎回流程测试'''
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
    def test_jjsh(self, data):
        '''基金赎回'''
        try:
            self.page.logger("登录-卖基金-卖出方式-卖出-撤单(检查)")
            self.page.denglu(data['用户名'], data['密码'])
            self.page = ShouyePage(self.page)
            self.page.caidan("我的")
            self.page = Mine(self.page)
            self.page.djcd("卖基金")
            self.page = MaiJiJin(self.page)
            kyfe = self.page.xzmjj(data["支付账号尾号"],data["基金代码"])
            self.page = MaiJiJinFangShi(self.page)
            self.page.xzshfs(data["赎回方式"])
            if data["赎回方式"] != "快速取现":
                if data["赎回方式"] == "基金转换":
                    self.page = Search(self.page)
                    self.page.search_zhxx(data["转入基金代码"])

                self.page = QXXiangQing(self.page)
                txzc = self.page.kemaichuzc()
                if kyfe in txzc:
                    self.page.logger("%s可用份额与可提现份额一致"%(data["基金代码"]))
                else:
                    raise AssertionError("%s可用份额与可提现份额一致"%(data["基金代码"]))
                if data["赎回方式"] == "银行卡":
                    self.page.djmc(data["赎回份额"], data["交易密码"])
                if data["赎回方式"] == "基金转换":
                    self.page.djzh(data["赎回份额"], data["交易密码"])
                if data["赎回方式"] == "普通取现":
                    self.page.djqx(data["赎回份额"], data["交易密码"])
                self.page.logger("%s成功" % (data["赎回方式"]))
                self.page = JiaoYiJieGuo(self.page)
                self.page.page_wancheng()
                self.page = Mine(self.page)
                self.page.jiaoyijilu()
                self.page = JiaoYiJiLu(self.page)
                self.page.qh_tab("可撤单")
                self.page.chakanxiangqing(0)
                self.page = JiaoYiXiangQing(self.page)
                self.page.chedan(data['交易密码'])
                self.page.logger("成功撤单%s赎回到%s" % (data["基金代码"],data["赎回方式"]))

            if data["赎回方式"] == "快速取现":
                self.page = QXXiangQing(self.page)
                self.page.djqx(data["赎回份额"], data["交易密码"])
                self.page.logger("%s成功" % (data["赎回方式"]))
                self.page = JiaoYiJieGuo(self.page)
                self.page.page_wancheng()
                self.page = Mine(self.page)
                self.page.jiaoyijilu()
                self.page = JiaoYiJiLu(self.page)
                self.page.jianchajiaoyi(0)
        except:
            self.page.logger("基金赎回失败")
            self.page.save_screen_shot("test_基金赎回")
            self.imgs.append(self.page.driver.get_screenshot_as_base64())
            self.page.logger(browser.Browser.creathtml(self,path = browser.picpath, pic = browser.pics))
            raise AssertionError("基金赎回失败")

if __name__ == '__main__':
    unittest.main()
