import unittest
from config.config import login_url
from utils import read_excel
from config import config
from ddt import ddt,data
from test.page.denglu_main_page import DendluMainPage
from test.page.shouye_page import ShouyePage
from test.page.mine_page import Mine
from test.page.xjbzichan_page import XJBZiChan
from test.page.maijijinfangshi_page import MaiJiJinFangShi
from test.page.qxxiangqing_page import QXXiangQing
from test.page.jiaoyijilu_page import JiaoYiJiLu
from test.page.jiaoyixiangqing_page import JiaoYiXiangQing
from test.page.jiaoyijieguo_page import JiaoYiJieGuo

test = read_excel.ExcelUtil(config.DATA_PATH + '\\现金宝取现.xlsx', 'test').next()
url = login_url

@ddt
class XJBShuHui(unittest.TestCase):
    '''现金宝赎回流程测试'''
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
    def test_xjbqx(self,data):
        '''现金宝取现'''
        try:

            self.page.logger("登录-现金宝-取现-撤单(检查)")
            self.page.denglu(data['用户名'], data['密码'])
            self.page = ShouyePage(self.page)
            self.page.caidan("我的")
            self.page = Mine(self.page)
            #获取我的页面现金宝资产
            xjbzc = self.page.djzc("现金宝")
            self.page = XJBZiChan(self.page)
            xjbzzc,xjbky = self.page.xjbzc()
            if xjbzzc == xjbzc:
                self.page.logger("里外现金宝资产一致")
            else:
                raise AssertionError("现金宝资产获取异常")
            self.page.dj_xjbbutton("取现")
            self.page = MaiJiJinFangShi(self.page)
            self.page.xzshfs(data["取现方式"])
            self.page = QXXiangQing(self.page)
            if data["取现方式"] == "普通取现":
                txzc = self.page.kemaichuzc()
                if xjbky in txzc:
                    self.page.logger("现金宝可用份额与可提现份额一致")
                else:
                    raise AssertionError("现金宝可提现份额异常")
                self.page.djqx(data["取现金额"],data["交易密码"])
                self.page.logger("现金宝%s成功"%(data["取现方式"]))
                self.page = JiaoYiJieGuo(self.page)
                self.page.page_wancheng()
                self.page = Mine(self.page)
                self.page.jiaoyijilu()
                self.page = JiaoYiJiLu(self.page)
                self.page.qh_tab("可撤单")
                self.page.chakanxiangqing(0)
                self.page = JiaoYiXiangQing(self.page)
                self.page.chedan(data['交易密码'])
                self.page.logger("成功撤单现金宝%s"%(data["取现方式"]))
            if data["取现方式"] == "快速取现":
                self.page.djqx(data["取现金额"], data["交易密码"])
                self.page.logger("现金宝%s成功" % (data["取现方式"]))
                self.page = JiaoYiJieGuo(self.page)
                self.page.page_wancheng()
                self.page = Mine(self.page)
                self.page.jiaoyijilu()
                self.page = JiaoYiJiLu(self.page)
                self.page.jianchajiaoyi(0)
        except:
            self.page.logger("现金宝%s失败"%(data["取现方式"]))
            self.page.save_screen_shot("test_现金宝%s失败"%(data["取现方式"]))
            self.imgs.append(self.page.driver.get_screenshot_as_base64())
            raise AssertionError("现金宝%s失败"%(data["取现方式"]))

if __name__ == '__main__':
    unittest.main()