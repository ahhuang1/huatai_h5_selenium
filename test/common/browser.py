import time
import os
#from appium import webdriver
from selenium import webdriver
from config.config import SCREEN_PATH
from utils.log import logger

mobileEmulation = {'deviceName' : 'Galaxy S5'}
# options = webdriver.ChromeOptions()
# options.add_experimental_option('mobileEmulation', mobileEmulation)
# driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
# wait = WebDriverWait(driver, 10)
picpath = []
pics = []
class Browser(object):

    def __init__(self):
        self.driver = None

    #获取浏览器是为手机h5页面调试模式，如果h5pange等于1，切换h5页面调试模式。默认等于1
    def get(self,url,h5page=1):
        if h5page != 1:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
            self.driver.get(url)
        else:
            self.options = webdriver.ChromeOptions()
            self.options.add_experimental_option('mobileEmulation', mobileEmulation)
            self.driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=self.options)
            self.driver.implicitly_wait(10)
            self.driver.get(url)
        return self

    #浏览器页面截图功能
    def save_screen_shot(self, name='screen_shot'):
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        screenshot_path = SCREEN_PATH + '\screenshot_%s' % day
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)

        tm = time.strftime('%H_%M_%S', time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screenshot_path + '\\%s_%s.jpg' % (tm, name))
        # print(screenshot)
        # pic = '%s_%s.jpg' % (name, tm)
        # path = screenshot_path + '\\%s_%s.jpg' % (name, tm)
        # pics.append(pic)
        # picpath.append(path)
        return screenshot


    # def creathtml(self,path, pic):
    #     html = ''
    #     if len(path) > 0:
    #         for i in range(len(path)):
    #             if i == 0:
    #                 html = '<a href=' + path[i] + ' target="_blank">' + pic[i] + '</a>'
    #             else:
    #                 html = html + '<br /><a href=' + path[i] + ' target="_blank">' + pic[i] + '</a>'
    #     else:
    #         html = ''
    #     htmls = 'htmlbegin<td>' + html + '</td>htmlend'
    #     return htmls

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()

    def logger(self,info):
        return logger.info(info)

    def action(self):
        action = webdriver.TouchActions(self.driver)
        return action

if __name__ == '__main__':
    b = Browser().get('http://www.baidu.com')
    time.sleep(3)
    b.save_screen_shot('test_登录')
    time.sleep(3)
    b.quit()