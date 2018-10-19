import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test.common.browser import Browser
from utils.log import logger
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

class Page(Browser):
    # 滑动元素定位
    loc_app_div = (By.XPATH, '//*[@id="app"]')
    #页面后退按钮
    loc_houtui_span = (By.XPATH,'//span[@class="mint-button-icon"]')
    #首页菜单项
    loc_home_div = (By.XPATH,'//div[@class="tab-title" and contains(text(),"首页")]')
    #市场菜单项
    loc_markets_div = (By.XPATH,'//div[@class="tab-title" and contains(text(),"市场")]')
    #自选菜单项
    loc_portfolio_div = (By.XPATH,'//div[@class="tab-title" and contains(text(),"自选")]')
    #资讯
    loc_news_div = (By.XPATH,'//div[@class="tab-title" and contains(text(),"资讯")]')
    #我的菜单项
    loc_mine_div = (By.XPATH,'//div[@class="tab-title" and contains(text(),"我的")]')
    #交易密码框
    loc_jiaoyimima_input = (By.XPATH, '//*[@type="password"]')
    # 交易确定框
    loc_queding_button = (By.XPATH, '//*[@class="message-box-btn confirm-btn"]')
    #付款方式
    loc_fukuan_div = (By.XPATH, '//div[contains(text(),"付款方式")]')
    # 支付方式标题（现金宝，货币A,银行卡）
    loc_zflb_div = (By.XPATH, '//div[@class="header"]/../div[2]/div')
    # 现金宝支付方式第一个银行卡元素
    loc_xzb_div = (By.XPATH, '//div[@class="xjb-item"]')
    # 现金宝银行卡列表
    loc_huobibanklists_div = (By.XPATH, '//*[@class="bankitem"]')
    #菜单标题
    loc_title_h = (By.XPATH,'//*[@class="mint-header-title"]')

    def __init__(self, page=None):
        if page:
            self.driver = page.driver
        else:
            super(Page, self).__init__()

    @property
    def current_window(self):
        return self.driver.current_window_handle

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url

    def get_driver(self):
        return self.driver

    def refresh(self):
        return self.driver.refresh()

    def wait(self, seconds=5):

        time.sleep(seconds)
        self.driver.implicitly_wait(10)

    def execute(self, js, *args):
        self.driver.execute_script(js, *args)

    def move_to(self, element):
        ActionChains(self.driver).move_to_element(element).perform()

    def find_element(self, *args):
        try:
            WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(args))
            return self.driver.find_element(*args)
        except:
            logger.info("%s 页面中未能找到 %s 元素"%(self, *args))
            self.save_screen_shot("test_页面元素未找到截图")
            raise AssertionError("元素没有找到")

    def find_elements(self, *args):
        # try:
        # WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(args))
        return self.driver.find_elements(*args)
        # except:
        #     logger.info("%s 页面中未能找到 %s 元素"%(self, *args))
        #     self.save_screen_shot("test_页面元素未找到截图")
        #     raise AssertionError("元素没有找到")


    def switch_to_window(self, partial_url='', partial_title=''):
        """切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则需要传入参数来确定要跳转到哪个窗口
        """
        all_windows = self.driver.window_handles
        if len(all_windows) == 1:
            logger.warning('只有1个window!')
        elif len(all_windows) == 2:
            other_window = all_windows[1 - all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if partial_url in self.driver.current_url or partial_title in self.driver.title:
                    break
        logger.debug(self.driver.current_url, self.driver.title)

    #切换ifram表单
    def switch_to_frame(self, param):
        self.driver.switch_to.frame(param)

    #切换浏览器弹框
    def switch_to_alert(self):
        return self.driver.switch_to.alert

    #获取新的url
    def get_newurl(self,url):
        return self.driver.get(url)

    # def getSize(self):
    #     x = self.driver.get_window_size()['width']
    #     y = self.driver.get_window_size()['height']
    #     return (x,y)
    #
    # def swipeDown(self,t,l):
    #     x1 = int(l[0] * 0.5)  # x坐标
    #     y1 = int(l[1] * 0.25)  # 起始y坐标
    #     y2 = int(l[1] * 0.75)  # 终点y坐标
    #     self.driver.swipe(x1, y1, x1, y2, t)

    #滑到到底部
    def huadong(self):
        self.action().scroll_from_element(self.find_element(*self.loc_app_div),0,1000).perform()
        self.wait()

    #页面后退按钮
    def houtui(self):
        self.wait(1)
        self.execute("arguments[0].click()",self.find_element(*self.loc_houtui_span))
        self.wait(3)

    #切换主页面菜单
    def caidan(self,caidanname):
        self.logger("切换至%s"%(caidanname))
        if caidanname == "首页":
            self.execute("arguments[0].click()", self.find_element(*self.loc_home_div))
        if caidanname == "市场":
            self.execute("arguments[0].click()", self.find_element(*self.loc_markets_div))
        if caidanname == "自选":
            self.execute("arguments[0].click()", self.find_element(*self.loc_portfolio_div))
        if caidanname == "资讯":
            self.execute("arguments[0].click()", self.find_element(*self.loc_news_div))
        if caidanname == "我的":
            self.execute("arguments[0].click()", self.find_element(*self.loc_mine_div))
        self.wait(6)

    #输入交易密码并确定
    def mmqd(self,password):
        self.logger("输入交易密码")
        self.find_element(*self.loc_jiaoyimima_input).send_keys(password)
        self.logger("点击确定按钮")
        self.find_element(*self.loc_queding_button).click()
        self.wait(6)

    #选择付款方式
    def xzfk(self,bank):
        try:
            self.execute("arguments[0].click()", self.find_element(*self.loc_fukuan_div))
            #self.find_element(*self.loc_fukuan_div).click()
            self.wait(2)
            xjb_len = len(self.find_elements(*self.loc_xzb_div))
            if xjb_len == 1:
                if bank in self.find_elements(*self.loc_xzb_div)[0].text:
                    self.logger("能够选择%s付款"%(bank))
                    self.find_elements(*self.loc_huobibanklists_div)[0].click()
                if bank not in self.find_elements(*self.loc_xzb_div)[0].text:
                    if bank == "现金宝" or bank == "其它货币":
                        self.logger("不支持%s支付方式"%(bank))
                        raise AssertionError("选择支付方式失败")
                    if bank =="银行卡":
                        self.logger("选择%s支付"%(bank))
                        self.find_elements(*self.loc_zflb_div)[1].click()

            if xjb_len == 0:
                self.logger("不支持现金宝或货币支付")
                if bank == "现金宝" or bank == "其它货币":
                    self.logger("不支持%s支付方式",bank)
                    raise AssertionError("选择支付方式失败")
                if bank == "银行卡":
                    self.logger("选择%s支付" % (bank))
                    self.find_elements(*self.loc_zflb_div)[0].click()


            if xjb_len == 2:
                if bank == "现金宝":
                    self.logger("能够选择%s付款" % (bank))
                    self.find_elements(*self.loc_huobibanklists_div)[0].click()
                if bank == "其它货币":
                    self.logger("能够选择%s付款" % (bank))
                    self.find_elements(*self.loc_huobibanklists_div)[-1].click()
                if bank == "银行卡":
                    self.logger("选择%s支付" % (bank))
                    self.find_elements(*self.loc_zflb_div)[-1].click()

            self.wait()
        except:
            self.logger("选择付款方式失败")
            self.save_screen_shot("test_付款方式")
            raise AssertionError("选择付款方式失败")

    #获取页面标题
    def page_title(self):
        title = self.find_element(*self.loc_title_h).text
        return title

