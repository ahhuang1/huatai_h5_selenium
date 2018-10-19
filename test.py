# class Fib(object):
#     def __init__(self):
#         self.a,self.b = 0,1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.a,self.b = self.b,self.a+self.b
#         if self.a > 100:
#             raise StopIteration()
#         return self.a
#
#     def __getitem__(self, item):
#         a,b = 1,1
#         for x in range(item):
#             a,b = b,a+b
#         return a
# for n in Fib():
#     print(n)
#
# f = Fib()
# print(f[0])
# print(f[60])


# class Fib1(object):
#     def __getitem__(self, item):
#         if isinstance(item,int):
#             a,b = 1,1
#             for x in range(item):
#                 a,b = b, a+b
#             return a
#         if isinstance(item,slice):
#             start = item.start
#             stop = item.stop
#             if start is None:
#                 start = 0
#             a,b = 1,1
#             L=[]
#             for x in range(stop):
#                 if x>=start:
#                     L.append(a)
#                 a,b = b,a+b
#             return L
#
# f = Fib1()
# print(f[0:5])
# print(f[:10])
#
# class Chain(object):
#     def __init__(self,path=''):
#         self._path = path
#
#     def __getattr__(self, path):
#         return Chain('%s/%s'%(self._path,path))
#
#     def __str__(self):
#         return self._path
#
#     __repr__ = __str__
#
# print(Chain().status.user.timeline.list)
#
# def fn(self,name='world'):
#     print('Hello,%s'%name)
#
# Hello = type('Hello',(object,),dict(hello=fn))
#
# h = Hello()
# h.hello()
# print(type(Hello))

# from functools import reduce
#
# def str2num(s):
#     return eval(s)
#
# def calc(exp):
#     ss = exp.split('+')
#     ns = map(str2num, ss)
#     return reduce(lambda acc, x: acc + x, ns)
#
# def main():
#     r = calc('100 + 200 + 345')
#     print('100 + 200 + 345 =', r)
#     r = calc('99 + 88 + 76')
#     print('99 + 88 + 7.6 =', r)
#
# main()

# class Dict(dict):
#     def __init__(self,**kw):
#         super().__init__(**kw)
#
#     def __getattr__(self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Dict' object has no attribute '%s'"% key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
#
# import unittest
# class TestDict(unittest.TestCase):
#
#     def test_init(self):
#         d = Dict(a=1,b='test')
#         self.assertEqual(d.a,1)
#         self.assertEqual(d.b,'test')
#         self.assertTrue(isinstance(d,dict))
#
#     def test_key(self):
#         d = Dict()
#         d['key'] = 'value'
#         self.assertEqual(d.key,'value')
#
#
#
#     def test_attr(self):
#         d= Dict()
#         d.key = 'value'
#         self.assertTrue('key' in d)
#         self.assertEqual(d['key'], 'value')
#
#     def test_keyerror(self):
#         d = Dict()
#         with self.assertRaises(KeyError):
#             value = d['empty']
#
#     def test_attrerror(self):
#         d= Dict()
#         with self.assertRaises(AttributeError):
#             value = d.empty
#
# if __name__ == '__main__':
#     unittest.main()
# try:
#     f = open(r'C:\Users\win8\Desktop\test.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()
# with open(r'C:\Users\win8\Desktop\test.txt','a') as f:
#     f.write('hello world ，黄爱华')
#
# from io import StringIO
# f = StringIO()
# print(f.write('hello'))
# print(f.write(''))
# print(f.write('hello!'))
# print(f.getvalue())


# from io import BytesIO
# f = BytesIO()
# print(f.write('中文'.encode('utf-8')))
# print(f.getvalue())

import os
# print(os.name)
# print(os.environ.get('PATH'))
# print(os.path.abspath('.'))
# mk = os.path.join(os.path.abspath(''),'TEST12')
# print(mk)
# print(os.path.split(mk))
# print(os.listdir('.'))
# print([x for x in os.listdir('.') if os.path.isdir(x)])
# print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] =='.py'])

# def get_dirtree(tadir):
#     return [d for d in os.walk(tadir)]
#
# def get_path_filename(path,filename):
#     for x in os.listdir(path):
#         x = os.path.join(path,x)
#         if os.path.isdir(x):
#             get_path_filename(x,filename)
#         else:
#             if filename in os.path.split(x)[1]:
#                 print(x)
#     return
#
# print(get_path_filename(os.path.abspath('.'),'test'))
#
#
# import json
# obj = dict(name='小明',age=20)
# s = json.dumps(obj,ensure_ascii=False)
# print(s)

# from datetime import datetime
# dt = datetime.now()
# print(dt)
# dt = dt.timestamp()
# print(dt)
# dt = datetime.fromtimestamp(dt)
# print(dt)
# print(dt.strftime('%a, %b %d %H:%M'))

# from collections import namedtuple
# Point = namedtuple('Point',['x','y'])
# p = Point(1,2)
# print(p.x)
# print(p.y)
#
# from collections import deque
# q = deque(['a','b','c'])
# q.append('d')
# q.appendleft('x')
# print(q)
# b = list([1,3,4])
# b.ap
#
# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['22'])

# from collections import OrderedDict
# d = dict([('a',1),('b',2),('c',3)])
# print(d)
# od = OrderedDict([('a',1),('b',2),('c',3)])
# print(od)
# print(od['b'])
# print(list(d.keys()))
# print(list(od.keys()))

# from collections import OrderedDict
#
# class LastUpdatedOrderedDict(OrderedDict):
#     def __init__(self,capacity):
#         super(LastUpdatedOrderedDict, self).__init__()
#         self._capacity = capacity
#
#     def __setitme__(self,key,value):
#         containsKey = 1 if key in self else 0
#         if len(self) - containsKey >= self._capacity:
#             last = self.popitem(last=False)
#             print('remove:',last)
#         if containsKey:
#             del self[key]
#             print('set:',(key,value))
#         else:
#             print('add:',(key,value))
#         OrderedDict.__setitem__(self,key,value)
#
# if __name__ == '__main__':
#
#     d = LastUpdatedOrderedDict(1)
#     d.__setitme__('a',3)
#     print(d['a'] == 1234)
#     d['b'] = 2444
#     d['c'] = 34334
#     print(d)
#     d['d'] = 4324324
#     print(d)
#     d['b'] = 534134
#     print(d)
# import chardet
# d = '我还是黄爱华'.encode('gbk')
# print(type(d))
# print(d)
# print(d.decode('gbk'))
# print(chardet.detect(d))

# import sqlite3
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# try:
#     cursor.execute('create table user(id varchar(20) PRIMARY key, name varchar(20))')
#     cursor.execute('insert into user(id,name) VALUES (\'1\',\'Michael\'),(\'2\',\'黄aihua\')')
#     print(cursor.rowcount)
# finally:
#     cursor.close()
#     conn.commit()
#     conn.close()
# conn = sqlite3.connect('test.db')
# cursor = conn.cursor()
# # 执行查询语句:
# cursor.execute('select * from user where id=? or id=?', ('1','2'))
# # 获得查询结果集:
# values = cursor.fetchall()
# print(values)
# cursor.close()
# conn.close()

# import os,sqlite3
#
# db_file = os.path.join(os.path.dirname(__file__),'test.db')
# if os.path.isfile(db_file):
#     os.remove(db_file)
#
# #初始数据
# conn = sqlite3.connect(db_file)
# curor = conn.cursor()
#
# curor.execute('create table user(id varchar(20) primary key,name varchar(20),score int)')
# curor.execute("insert into user values('A-001','AIHUA',95),('A-002','黄爱华',55),('A-003','HAH',65)")
# curor.execute("SELECT * FROM user")
# print(curor.fetchall())
# curor.close()
# conn.commit()
# conn.close()
#
# def get_score_in(low,high):
#     conn = sqlite3.connect(db_file)
#     curor = conn.cursor()
#     curor.execute("select * from user where score <= ? and score>= ? order by score",(high,low))
#     scores = curor.fetchall()
#     curor.close()
#     conn.close()
#     return [score[1] for score in scores]
#
# assert get_score_in(80, 95) == ['AIHUA'], get_score_in(80, 95)
# assert get_score_in(50, 70) == ['黄爱华', 'HAH'], get_score_in(50, 70)
# assert get_score_in(50, 100) == ['黄爱华', 'HAH','AIHUA'], get_score_in(50, 100)
# print(get_score_in(80,95))
# print(get_score_in(50,70))
# print(get_score_in(50,100))
# print('Pass')

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
# Base = declarative_base()
# # 定义User对象:
# class User(Base):
#     # 表的名字:
#     __tablename__ = 'user'
#
#     # 表的结构:
#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#
# # 初始化数据库连接:
# #engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
# engine = create_engine('sqlite:///:memory:',echo=True)
# # 创建DBSession类型:
# DBSession = sessionmaker(bind=engine)

from selenium import webdriver
import time
# str ={
# 'BAIDUID':'1B2EB797B17A13C06CEF466BC1CDD2E3:FG=1',
# 'PSTM':'1525834876',
# 'BIDUPSID':'0B5F3BE81FF9862F4F5E357951E4D82F',
# 'cflag':'15%3A3',
# 'BDRCVFR[IZdXtXdDRBm]':'yiTPYW-i3eTXZFWmv68mvqV',
# 'BDRCVFR[yfg8b4Gp7xm]':'yiTPYW-i3eTXZFWmv68mvqV',
# 'BDRCVFR[KKxQ_aGZ5eD]':'yiTPYW-i3eTXZFWmv68mvqV',
# 'PHPSESSID':'gqe968dm6d17d3ohlomfobenj1',
# 'PSINO':'3',
# 'H_PS_PSSID':'1429_21105_27112',
# 'BDORZ':'B490B5EBF6F3CD402E515D22BCDA1598',
# 'Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04':'1535625643,1535625656,1535640362',
# 'BDUSS':'TZETWFmMUwtWn50M2hjRlBGNmhweGJJR3QxNUtHQkJIRU9wa3lzcEo1ZGxrSzliQUFBQUFBJCQAAAAAAAAAAAEAAAAP6JBPs6y8truqMTExAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGUDiFtlA4hbY',
# 'Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04':'1535640422',
# }
# driver = webdriver.Chrome()
# driver.get('https://www.baidu.com/')
# driver.delete_all_cookies()
#
# for k,v in str.items():
#     print('k:',k,'===','v:',v)
#     a = int(time.time())
#     cookie_dict = {
#         "domain": ".baidu.com",
#         'name': k,
#         'value': v,
#         "expires": a,
#         'path': '/',
#         'httpOnly': False,
#         'HostOnly': False,
#         'Secure': False}
#     driver.add_cookie(cookie_dict=cookie_dict)
# print(driver.get_cookies())
# print(len(driver.get_cookies()))
# driver.get('http://i.baidu.com/')
# print('===================================')
# print(driver.get_cookies())
# print('===================================')
# print(len(driver.get_cookies()))
# time.sleep(5)
# import pickle
# driver = webdriver.Chrome()
# # driver.get(url='http://i.baidu.com/my/history')
# # time.sleep(60)
# # driver.refresh()
# # b = driver.get_cookies()
#
# # print(b)
# # pickle.dump(b,open("cookies.pkl","wb"))
# driver.get("http://www.baidu.com")
# driver.refresh()
# driver.delete_all_cookies()
# cookies = pickle.load(open("cookies.pkl","rb"))
# time.sleep(5)
# # driver.delete_all_cookies()
# for cookie in cookies:
#     print(cookie)
#     driver.add_cookie(cookie)
#     time.sleep(3)
# time.sleep(3)
# driver.get(url='http://i.baidu.com/my/history')
# time.sleep(60)

# b = {'a':2,'c':'sdfads','d':{'1':'aa','2':'b','3':{}}}
# import json
# c = json.dumps(b,indent=4)
# print(c)

# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.action_chains import ActionChains
#
# driver = webdriver.Chrome()
# driver.get('https://china-testing.github.io/category/python.html')
# driver.implicitly_wait(30)
# time.sleep(3)
# driver.find_element_by_xpath('//a[text()="数据分析"]').click()
# time.sleep(3)
# element = driver.find_element_by_xpath('//a[text()="python"]')
# ActionChains(driver).key_down(Keys.CONTROL).click(element).key_up(Keys.CONTROL).perform()
# time.sleep(3)
# current = driver.current_window_handle
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(2)
# driver.close()
# driver.switch_to.window(current)
# time.sleep(3)
# driver.quit()


# import unittest
# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
#
# class ToolTest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://jqueryui.com/tooltip/")
#         self.driver.implicitly_wait(20)
#         self.driver.maximize_window()
#
#     def test_tool_tip(self):
#         time.sleep(3)
#         frame_elm = self.driver.find_element_by_class_name('demo-frame')
#         self.driver.switch_to.frame(frame_elm)
#         ActionChains(self.driver).move_to_element(self.driver.find_element_by_id('age')).perform()
#         time.sleep(3)
#         tool = WebDriverWait(self.driver,20).until(
#             expected_conditions.visibility_of_element_located(
#                 (By.CLASS_NAME,'ui-tooltip-content')
#             )
#         )
#
#         self.assertEqual('We ask for your age only for statistical purposes.',tool.text)
#
#         time.sleep(3)
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import unittest
#
# class dubaltest(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get('http://api.jquery.com/dblclick/')
#         self.driver.implicitly_wait(20)
#         self.driver.maximize_window()
#
#     def test_dubal_click(self):
#         time.sleep(2)
#         ele = self.driver.find_element_by_tag_name('iframe')
#         self.driver.switch_to.frame(ele)
#         time.sleep(2)
#         box = self.driver.find_element_by_xpath('//div')
#         self.assertEqual('rgba(0, 0, 255, 1)',box.value_of_css_property('background-color'))
#
#         ActionChains(self.driver).move_to_element(box).double_click(box).perform()
#
#         time.sleep(2)
#         self.assertEqual('rgba(255, 255, 0, 1)',box.value_of_css_property('background-color'))
#
#     def tearDown(self):
#         self.driver.close()
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

#

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# class at_least_n_elements_found(object):
#     def __init__(self, locator, n):
#         self.locator = locator
#         self.n = n
#
#     def __call__(self, driver):
#         elements = driver.find_elements(*self.locator)
#         if len(elements) >= self.n:
#             return elements
#         else:
#             return False
#
# url = 'http://www.webscrapingfordatascience.com/complexjavascript/'
# driver = webdriver.Chrome()
# driver.get(url)
# # Use an implicit wait for cases where we don't use an explicit one
# driver.implicitly_wait(10)
# div_element = driver.find_element_by_class_name('infinite-scroll')
# quotes_locator = (By.CSS_SELECTOR, ".quote:not(.decode)")
#
# nr_quotes = 0
# while True:
#
#     # Scroll down to the bottom, now using action (chains)
#     action_chain = ActionChains(driver)
#     # Move to our quotes block
#     action_chain.move_to_element(div_element)
#     # Click it to give it focus
#     action_chain.click()
#     # Press the page down key about 10 ten times
#     action_chain.send_keys([Keys.PAGE_DOWN for i in range(10)])
#     # Do these actions
#     action_chain.perform()
#
#     # Try to fetch at least nr_quotes+1 quotes
#     try:
#         all_quotes = WebDriverWait(driver, 3).until(
#             at_least_n_elements_found(quotes_locator, nr_quotes + 1))
#     except TimeoutException as ex:
#         # No new quotes found within 3 seconds, assume this is all there is
#         print("... done!")
#         break
#
#     # Otherwise, update the quote counter
#     nr_quotes = len(all_quotes)
#     print("... now seeing", nr_quotes, "quotes")
#
# # all_quotes will contain all the quote elements
# print(len(all_quotes), 'quotes found\n')
# for quote in all_quotes:
#     print(quote.text)
# input('Press ENTER to close the automated browser')
# driver.quit()

class a():
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __call__(self, *args, **kwargs):
        print(self.a)
        print(type(self.a))
        print(*self.a)
        print(type(*self.a))

A = a('1','2')
A()
B = a('2','3')
B()