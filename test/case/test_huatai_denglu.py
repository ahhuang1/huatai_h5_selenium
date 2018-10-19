import unittest
from config.config import login_url
from utils import read_excel
from config import config
from ddt import ddt,data
from test.page.denglu_main_page import DendluMainPage
from test.page.shouye_page import ShouyePage


test = read_excel.ExcelUtil(config.DATA_PATH + '\\登录用例.xlsx', 'test').next()
url = login_url

@ddt
class dengluTest(unittest.TestCase):
    '''华泰登录测试'''
    @classmethod
    def setUpClass(self):
        self.page = DendluMainPage().get(url)
    @data(*test)
    def test_denglu(self,data):
        '''正常登陆'''
        #self.imgs = []
        try:
            self.page.denglu(data['用户名'],data['密码'])
            self.page = ShouyePage(self.page)
            self.page.dengluzhuangtai(data["用户姓"])
        except:
            self.page.logger("登录失败")
            self.page.save_screen_shot("test_登录")#用来保存截图报本地
            self.imgs.append(self.page.driver.get_screenshot_as_base64())#用来保存截图展示在html中
            raise AssertionError("登录失败")

    def tearDown(self):
        self.page.refresh()
        self.page.get_newurl(url)
        self.page = DendluMainPage(self.page)

    @classmethod
    def tearDownClass(self):
        self.page.quit()

if __name__ == '__main__':
    unittest.main()
