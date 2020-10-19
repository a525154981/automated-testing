import os, configparser
from utils import setting


con = configparser.ConfigParser()
con.read(setting.CONFIG_DIR, encoding='utf-8')

class Config(object):

    def get(self):
       pass

def get_test_url():
    '''
    从配置文件中获得测试网址
    :return:
    '''
    url = con.get("WebURL", "URL")
    return url
print(get_test_url())
def get_login_name_and_pwd():
    '''
    从配置文件中获得测试账号跟密码
    :return:
    '''
    username = con.get('Internet', 'LOGIN_NAME')
    password = con.get('Internet', 'LOGIN_USER')
    return {'username': username, 'password': password}

def get_email_info(self):
    '''
    从配置文件中获得邮件发送模块相关配置信息
    :return:
    '''
    HOST = con.get("user", "HOST_SERVER")
    SENDER = con.get("user", "FROM")
    RECEIVER = con.get("user", "TO")
    USER = con.get("user", "user")
    PWD = con.get("user", "password")
    SUBJECT = con.get("user", "SUBJECT")

    return {'HOST':HOST, 'SENDER':SENDER, 'RECEIVER':RECEIVER,
            'USER':USER, 'PWD':PWD, 'SUBJECT':SUBJECT}

def get_test_mysql_info(self):
    '''
    从配置文件中获得mysql数据库连接相关配置信息
    :return:
    '''
    IP = con.get("Mysql", "IP")
    PORT = con.get("Mysql", "PORT")
    USER = con.get("Mysql", "USER")
    PASSWORD = con.get("Mysql", "PASSWORD")
    DB_NAME = con.get("Mysql", "DB_NAME")
    CHARSET = con.get("Mysql", "CHARSET")

    return {'IP': IP, 'PORT': PORT, 'USER': USER,
            'PASSWORD': PASSWORD, 'DB_NAME': DB_NAME, 'CHARSET': CHARSET}

def get_test_mssql_info(self):
    '''
    从配置文件中获得sqlserver数据库相关配置信息
    :return:
    '''
    IP = con.get("SqlServer", "IP")
    PORT = con.get("SqlServer", "PORT")
    USER = con.get("SqlServer", "USER")
    PASSWORD = con.get("SqlServer", "PASSWORD")
    DB_NAME = con.get("SqlServer", "DB_NAME")
    CHARSET = con.get("SqlServer", "CHARSET")

    return {'IP': IP, 'PORT': PORT, 'USER': USER,
            'PASSWORD': PASSWORD, 'DB_NAME': DB_NAME, 'CHARSET': CHARSET}








