import unittest
from test.page.shouye_page import ShouyePage

url = "https://e.huatai-pb.com/ht_wx/index.html#/index"

class ShouYe(unittest.TestCase):
    '''首页页面跳转测试'''
    @classmethod
    def setUpClass(self):
        self.page = ShouyePage().get(url)
        self.page.wait()

    @classmethod
    def tearDownClass(self):
        self.page.quit()

    def tearDown(self):
        self.page.refresh()
        self.page.get_newurl(url)
        self.page.wait(1)

    def test_cdtz(self):
        '''首页快捷菜单跳转'''
        try:
            self.page.sycd()

        except:
            self.page.save_screen_shot("test_首页跳转")  # 用来保存截图报本地
            self.imgs.append(self.page.driver.get_screenshot_as_base64())
            raise AssertionError("首页快捷菜单跳转异常")

if __name__ == '__main__':
    unittest.main()