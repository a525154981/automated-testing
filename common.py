import os, sys
import time
import requests
from pathlib import Path
import random
from faker import Faker
import configparser

from utils import setting

fake = Faker('zh_cn')


def get_now_time():
    '''
    获得当前时间
    :return:
    '''
    now = time.strftime("%Y-%m-%d_%H_%M_%S_")
    return now

def get_new_report(testreport):
    '''
    生成最新的测试报告文件
    :param testreport:
    :return: 返回文件
    '''
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    return file_new

"""一些生成器方法，生成随机数，手机号，以及连续数字等"""

def get_random_phone_number():
    """随机手机号"""
    return fake.phone_number()

def get_random_country():
    '''随机国家'''
    return fake.country()

def get_random_city():
    '''随机城市'''
    return fake.city()

def get_random_city_suffix():
    '''随机县'''
    return fake.city_suffix()

def get_random_address():
    """随机地址"""
    return fake.address()

def get_random_street_address():
    '''街道'''
    return fake.street_address()

def get_random_street_name():
    '''街道名'''
    return fake.street_name()

def get_random_postcode():
    '''邮编'''
    return fake.postcode()

def get_random_latitude():
    '''维度'''
    return fake.latitude()

def get_random_longitude():
    '''经度'''
    return fake.longitude()

def get_random_name():
    """随机姓名"""
    return fake.name()

def get_random_last_name():
    '''姓'''
    return fake.last_name()

def get_random_first_name():
    '''名'''
    return fake.first_name()

def get_random_name_male():
    '''男性姓名'''
    return fake.name_male()

def get_random_last_name_male():
    '''男性姓'''
    return fake.last_name_male()

def get_random_first_name_male():
    '''男性名'''
    return fake.first_name_male()

def get_random_name_female():
    '''女性姓名'''
    return fake.name_female()

def get_random_ean8():
    '''8位条码'''
    return fake.ean8()

def get_random_ean13():
    '''13位条码'''
    return fake.ean13()

def get_random_ean():
    '''自定义位数条码,只能选8或者13'''
    return fake.ean(length=8)

def get_random_company():
    '''公司名'''
    return fake.company()

def get_random_company_suffix():
    '''公司名后缀'''
    return fake.company_suffix()

def get_random_credit_card_number():
    '''卡号'''
    return fake.credit_card_number(card_type=None)

def get_random_credit_card_provider():
    '''卡的提供者'''
    return fake.credit_card_provider(card_type=None)

def get_random_credit_card_security_code():
    '''卡的安全密码'''
    return fake.credit_card_security_code(card_type=None)

def get_random_credit_card_expire():
    '''卡的有效期'''
    return fake.credit_card_expire()

def get_random_credit_card_full():
    '''完整卡信息'''
    return fake.credit_card_full(card_type=None)

def get_random_currency_code():
    '''货币代码'''
    return fake.currency_code()

def get_random_date_time():
    '''随机日期时间'''
    return fake.date_time(tzinfo=None)

def get_random_iso8601():
    '''以iso8601标准输出的日期'''
    return fake.iso8601(tzinfo=None)

def get_random_date_time_this_month():
    '''本月的某个日期'''
    return fake.date_time_this_month(before_now=True, after_now=False, tzinfo=None)

def get_random_date_time_this_year():
    '''本年的某个日期'''
    return fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)

def get_random_date_time_this_decade():
    '''本年代内的一个日期'''
    return fake.date_time_this_decade(before_now=True, after_now=False, tzinfo=None)

def get_random_date_time_this_century():
    '''本世纪一个日期'''
    return fake.date_time_this_century(before_now=True, after_now=False, tzinfo=None)

def get_random_date_time_between():
    '''两个时间间的一个随机时间'''
    return fake.date_time_between(start_date="-30y", end_date="now", tzinfo=None)

def get_random_timezone():
    '''时区'''
    return fake.timezone()

def get_random_time():
    '''时间（可自定义格式）'''
    return fake.time(pattern="%H:%M:%S")

def get_random_am_pm():
    '''随机上午下午'''
    return fake.am_pm()

def get_random_month():
    '''随机月份'''
    return fake.month()

def get_random_month_name():
    '''随机月份名字'''
    return fake.month_name()

def get_random_year():
    '''随机年'''
    return fake.year()

def get_random_day_of_week():
    '''随机星期几'''
    return fake.day_of_week()

def get_random_day_of_month():
    '''随机月中某一天'''
    return fake.day_of_month()

def get_random_time_delta():
    '''随机时间延迟'''
    return fake.time_delta()

def get_random_date_object():
    '''随机日期对象'''
    return fake.date_object()

def get_random_time_object():
    '''随机时间对象'''
    return fake.time_object()

def get_random_unix_time():
    '''随机unix时间（时间戳'''
    return fake.unix_time()

def get_random_date():
    '''随机日期（可自定义格式'''
    return fake.date(pattern="%Y-%m-%d")

def get_random_date_time_ad():
    '''公元后随机日期'''
    return fake.date_time_ad(tzinfo=None)

def get_random_job():
    '''工作职位'''
    return fake.job()

def get_random_text():
    '''随机生成一篇文章'''
    return fake.text(max_nb_chars=200)

def get_random_word():
    '''随机单词'''
    return fake.word()

def get_random_words():
    '''随机生成几个字'''
    return fake.words(nb=3)

def get_random_sentence():
    '''随机生成一个句子'''
    return fake.sentence(nb_words=6, variable_nb_words=True)

def get_random_sentences():
    '''随机生成几个句子'''
    return fake.sentences(nb=3)

def get_random_paragraph():
    '''随机生成一段文字(字符串)'''
    return fake.paragraph(nb_sentences=3, variable_nb_sentences=True)

def get_random_paragraphs():
    '''随机生成成几段文字(列表)'''
    return fake.paragraphs(nb=3)

def get_random_password():
    '''随机密码（可指定密码策略)'''
    return fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

def get_random_uuid4():
    '''随机uuid'''
    return fake.uuid4()

def get_random_locale():
    '''随机本地代码'''
    return fake.locale()

def get_random_phonenumber_prefix():
    '''运营商号段，手机号码前三位'''
    return fake.phonenumber_prefix()

def get_random_pyint():
    '''随机int'''
    return fake.pyint()

def get_random_pystr():
    '''随机字符串（可指定长度）'''
    return fake.pystr(min_chars=None, max_chars=20)

def get_random_user_agent():
    '''伪造UA'''
    return fake.user_agent()

def get_random_num(length):
    """随机数字"""
    return fake.random_number(length)

def get_random_email():
    """随机email"""
    return fake.email()

def get_random_ipv4():
    """随机IPV4地址"""
    return fake.ipv4()

def get_random_str(min_chars=0, max_chars=8):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)

def get_random_id_card():
    return fake.ssn()

def factory_generate_ids(starting_id=1, increment=1):
    """ 返回一个生成器函数，调用这个函数产生生成器，从starting_id开始，步长为increment。 """
    def generate_started_ids():
        val = starting_id
        local_increment = increment
        while True:
            yield val
            val += local_increment
    return generate_started_ids

def factory_choice_generator(values):
    """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """
    def choice_generator():
        my_list = list(values)
        rand = random.Random()
        while True:
            yield random.choice(my_list)
    return choice_generator


if __name__ == '__main__':
    for i in range(1):
        print(get_random_company(), get_random_name(), get_random_phone_number(), 123, 'Ko0muw9mxpn4mKcd40W0gw==')
        print(get_random_name(), get_random_phone_number(), get_random_id_card())
    # count = 0
    # while True:
    #     id_card = get_random_id_card()
    #     if int('0819') < int(id_card[10:14]) <= int('0831'):
    #         print(id_card)
    #         break







