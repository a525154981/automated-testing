import time, os, sys
from functools import wraps
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from utils.logger import Logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *
from utils.config import Config, get_login_name_and_pwd

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from utils.common import *

if not os.path.exists(setting.TEST_SCREENSHOT):os.mkdir(setting.TEST_SCREENSHOT)


logger = Logger(logger='Common_action').getlog()


QUEDING = (By.CLASS_NAME, 'layui-layer-btn0')
QUXIAO = (By.CLASS_NAME, 'layui-layer-btn1')


class Common_action(object):

    def __init__(self, driver = 'Chrome'):
        self.driver = driver
        self.config = Config()

    def open_browser(self, url):
        global browser
        driver = self.config.get()
        if driver:
            self.driver = driver
        logger.info("选择的浏览器为: %s 浏览器" % self.driver)
        if self.driver == 'Firefox':
            browser = webdriver.Firefox()
            logger.info("启动火狐浏览器")

        elif self.driver == 'Chrome':
            chrome_options = Options()
            chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
            chrome_options.add_argument('--start-maximized')  # 指定浏览器分辨率
            chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
            chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
            # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
            chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('lang=zh_CN.UTF-8')
            browser = webdriver.Chrome(options=chrome_options)
            browser = webdriver.Chrome()
            logger.info("启动谷歌浏览器")

        elif self.driver == 'IE':
            browser = webdriver.Ie()
            logger.info("启动IE浏览器")

        browser.get(url)
        logger.info("打开URL: %s" % url)
        browser.maximize_window()
        logger.info('全屏当前窗口')
        browser.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        return browser

    def close_browser(self):
        try:
            logger.info("关闭浏览器")
            browser.close()
        except NameError as e:
            logger.error('关闭浏览器窗口失败: %s' % e)

    def quit(self):
        browser.quit()

    def login(self, *loc):
        '''如果网页要登陆，需要先执行此操作'''
        try:
            username = get_login_name_and_pwd()['username'] #读取配置文件获得登录账号
            password = get_login_name_and_pwd()['password'] #读取配置文件获得登录密码
            browser.find_element(*loc[0]).send_keys(username)
            browser.find_element(*loc[1]).send_keys(password)
            browser.find_element(*loc[2]).click()
            logger.info('登录成功，登录账号为：%s' % username)
        except Exception as e:
            logger.info('登录失败: %s' % e)

    def check_and_click_login_alert(self):
        if self.is_visibility((By.XPATH, '//*[@id="layui-layer1"]')):
            self.click(QUEDING)



    def get_page_url(self):
        """获取当前页面的url"""
        logger.info('当前页面的url为:%s' % browser.current_url)

        return browser.current_url

    def get_page_title(self):
        """获取当前页面的title"""
        logger.info('当前页面的title为:%s' % browser.title)
        return browser.title

    def find_element(self, loc):
        try:
            # 元素可见时，返回查找到的元素；以下入参为元组的元素，需要加*
            WebDriverWait(browser, 30).until(lambda driver: driver.find_element(*loc).is_displayed())
            return browser.find_element(*loc)
        except NoSuchElementException:
            logger.warning('找不到定位元素: %s' %loc[1])
            raise
        except TimeoutException:
            logger.warning('查找元素超时：%s' % loc[1])
            raise

    def find_elements(self, *loc):
        try:
            WebDriverWait(browser, 30).until(lambda browser:browser.find_elemets(*loc).is_displayed())
            return browser.find_elements(*loc)
        except NoSuchElementException:
            logger.warning('找不到定位元素：%s'%loc[1])
            raise
        except TimeoutException:
            logger.warning('查找元素超时：%s' %loc[1])
            raise

    def clear(self, *loc):
        element = browser.find_element(*loc)
        try:
            element.clear()
            logger.info('清空文本框内容')
        except NameError as e:
            logger.error('清空文本框内容失败:%s'% e)


    def click(self, loc):
        logger.info('点击元素by %s: %s...' % (loc[0], loc[1]))
        try:
            self.find_element(loc).click()
            time.sleep(2)
        except AttributeError as e:
            logger.error('无法点击元素: %s' % e)
            raise

    def send_keys(self, loc, text):
        logger.info('清空文本框内容：%s...' %loc[1])
        self.find_element(loc).clear()
        time.sleep(1)
        logger.info('输入内容方式 by %s: %s....' % (loc[0], loc[1]))
        logger.info('输入的内容： %s' % text)
        try:
            self.find_element(loc).send_keys(text)
            time.sleep(1)
        except Exception as e:
            logger.error('输入内容失败 %s' % e)

    def get_screen_to_img(self, value):
        """将页面截图下来"""
        # file_path = setting.TEST_REPORT + '/'
        img_name = os.path.join(setting.TEST_SCREENSHOT, value + '.png')
        # img_name = file_path + value + '.png'
        try:
            browser.get_screenshot_as_file(img_name)
            browser.get_screenshot_as_png()
            logger.info("页面已截图,截图的路径在项目:%s"% img_name)
            print(img_name)
        except NameError as e:
            logger.error("失败截图%s" % e)
            self.get_screen_to_img(value)

    def get_error_screen_shot(function):
        @wraps(function)
        def get_screen_img(self, *args, **kwargs):
            try:
                result = function(self, *args, **kwargs)
                logger.info("%s 脚本运行正常" % function.__name__)
                return result
            except:
                Common_action().get_screen_to_img(function.__name__)
                raise
        return get_screen_img

    def move_to_element(self, loc):
        """鼠标悬停操作"""
        element = self.find_element(loc)
        ActionChains(browser).move_to_element(element).perform()

    def context_click(self, loc):
        """鼠标悬停操作"""
        element = self.find_element(loc)
        ActionChains(browser).context_click(element).perform()

    def back(self):
        """
        浏览器返回窗口
        """
        browser.back()
        logger.info('返回上一个页面')

    def forward(self):
        """
        浏览器前进下一个窗口
        """
        browser.forward()
        logger.info('前进到下一个页面')

    def wait(self, seconds):
        browser.implicitly_wait(seconds)
        logger.info("等待 %d 秒" % seconds)

    def get_text(self, loc):
        element = self.find_element(loc)
        return element.text

    def get_attribute(self, loc, name):
        element = self.find_element(loc)
        return element.get_attribute(name)

    def execute_js(self, js):
        return browser.execute_script(js)

    def js_focus_element(self, loc):
        target = self.find_element(*loc)
        browser.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = 'window.scrollTo(0,0)'
        browser.execute_script(js)

    def js_scroll_end(self):
        '''滚动到底部'''
        js = 'window.scrollTo(0,document.body.scrollHeight)'
        browser.execute_script(js)

    def select_by_index(self, loc, index):
        '''通过索引,index是索引第几个，从0开始'''
        element = self.find_element(loc)
        Select(element).select_by_index(index)

    def select_by_value(self, loc, value):
        '''通过value属性'''
        element = self.find_element(*loc)
        Select(element).select_by_value(value)

    def select_by_text(self, loc, text):
        '''通过文本值定位'''
        element = self.find_element(*loc)
        Select(element).select_by_value(text)

    def is_text_in_element(self, loc, text, timeout=10):
        try:
            result = WebDriverWait(browser, timeout, 1).until(EC.text_to_be_present_in_element(loc, text))
        except TimeoutException:
            logger.info('元素没有定位到:' + str(loc))
            return False
        else:
            return result

    def is_text_in_value(self, loc, value, timeout = 10):
        """判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值"""
        try:
            result = WebDriverWait(browser, timeout, 1).until(
                EC.text_to_be_present_in_element_value(loc, value))
        except TimeoutException:
            logger.info('元素没有定位到：' + str(loc))
            return False
        else:
            return result

    def is_title(self, loc, title, timeout = 10):
        result = WebDriverWait(browser, timeout, 1).until(EC.title_is(title))
        return result

    def is_title_contains(self, title, timeout = 10):
        result = WebDriverWait(browser, timeout, 1).until(EC.title_contains(title))
        return result

    def is_selected(self, loc, timeout = 10):
        '''判断元素被选中，返回布尔值'''
        result = WebDriverWait(browser, timeout, 1).until(EC.element_located_to_be_selected(loc))
        return result

    def is_selected_be(self, loc, selected = True, timeout = 10):
        '''判断元素的状态，selected是期望的参数True/False
        返回布尔值
        '''
        result = WebDriverWait(browser, timeout, 1).until(EC.element_located_selection_state_to_be(loc, selected))
        return result

    def is_alert_present(self, timeout=10):
        '''
        判断页面是否有alert
        有返回alert(这里返回alert,不是True)
        没有返回False
        '''
        result = WebDriverWait(browser, timeout, 1).until(EC.alert_is_present())
        return result

    def is_visibility(self, loc, timeout = 10):
        '''元素可见返回本身，不可见返回false'''
        try:
            result = WebDriverWait(browser, timeout, 1).until(EC.visibility_of_element_located(loc))
            logger.info('返回的元素为 %s' % result)
            return result
        except:
            logger.info('此账号没有被登录')

    def is_invisibility(self, loc, timeout = 10):
        '''元素可见返回本身，不可见返回True,没找到元素也返回True'''
        result = WebDriverWait(browser, timeout, 1).until(EC.invisibility_of_element_located(loc))
        return result

    def is_clickable(self, loc, timeout = 10):
        '''元素可以点击is_enabled返回本身，不可点击返回false'''
        result = WebDriverWait(browser, timeout, 1).until(EC.element_to_be_clickable(loc))
        return result

    def is_located(self, loc, timeout = 10):
        '''判断元素有没有被定位到（并不意味着可见），定位到返回element，没定位到返回False'''
        result = WebDriverWait(browser, timeout, 1).until(EC.presence_of_element_located(loc))
        return result

    def clcik_alert_window(self):
        '''操作点击弹窗'''
        alert = browser.switch_to.alert
        time.sleep(2)
        alert.accept()
        time.sleep(2)

    def get_alert_text(self):
        """返回弹窗的文本内容"""
        alert = browser.switch_to.alert
        rel = alert.text
        return rel

    def switch_to_iframe(self, loc):
        """
        多表单嵌套切换
        :param loc: 传元素的属性值
        :return: 定位到的元素
        """
        try:
            logger.info('切换到 %s 标签下' %loc)
            return browser.switch_to_frame(loc)
        except NoSuchFrameException as msg:
            logger.error("查找iframe异常-> {0}".format(msg))

    def get_current_window(self):
        ''''''
        return browser.window_handles

    def switch_to_default_content(self):
        ''''''
        return browser.switch_to.default_content()

    def switch_windows(self, loc):
        """
        多窗口切换
        :param loc:
        :return:
        """
        try:
            return browser.switch_to_window(loc)
        except NoSuchWindowException as msg:
            logger.error("查找窗口句柄handle异常-> {0}".format(msg))

    def perform_add(self):
        pass

    def perform_edit(self):
        pass

    def perform_delete(self):
        pass


















