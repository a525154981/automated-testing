'''
此处为日志模块，可以根据业务需求，选择记录需要的执行日志信息
'''
import logging
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from utils.common import *

if not os.path.exists(setting.LOG_DIR):os.mkdir(setting.LOG_DIR)

class Logger(object):

    def __init__(self, logger):
        #创建一个logger文件
        self.logger = logging.getLogger(logger)
        # 指定日志的最低输出级别，默认为WARN级别
        # DEBUG，INFO，WARNING，ERROR，CRITICAL
        self.logger.setLevel(logging.DEBUG)

        #创建一个log文件夹
        log_name = os.path.join(setting.LOG_DIR, '%s.log' % get_now_time())
        #创建一个handler, 用来写入日志文件
        file_handle = logging.FileHandler(filename=log_name, encoding='utf-8')
        file_handle.setLevel(logging.INFO)

        #控制台日志
        control_handle = logging.StreamHandler(sys.stdout)
        control_handle.setLevel(logging.INFO)

        # 将输出的hangdle格式进行转换
        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        file_handle.setFormatter(formatter)
        control_handle.setFormatter(formatter)

        # 给logger添加handle
        self.logger.addHandler(file_handle)
        self.logger.addHandler(control_handle)

    def getlog(self):
        return self.logger








































