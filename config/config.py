import os

login_url='https://e.huatai-pb.com/ht_wx/index.html#/login'
# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
DATA_PATH = os.path.join(BASE_PATH, 'data')
#DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH, 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report\\report_html')
SCREEN_PATH = os.path.join(BASE_PATH, 'report')
TEST_CASE = os.path.join(BASE_PATH,'test\\case')
