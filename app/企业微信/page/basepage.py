"""
存放基本的方法，比如：初始化driver,find查找元素
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        logging.info(f'find:{locator}')
        return self.driver.find_element(*locator)  # *是用来解包的，传过来是元组的形式

    def find_and_click(self, locator):
        logging.info(f'find_and_click:{locator}')
        self.find(locator).click()  # 调用本地封装的find方法

    def find_and_sendkeys(self, locator, text):
        logging.info(f'find_and_sendkeys:{text}')
        self.find(locator).send_keys(text)

    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        'new UiScrollable'
                                        '(new UiSelector().'
                                        'scrollable(true).'
                                        'instance(0)).'
                                        'scrollIntoView('
                                        'new UiSelector().'
                                        f'text("{text}").instance(0));')

    def webderiver_wait(self, locator, timeout=10):
        logging.info(f'webderiver_wait:{locator},timeout:{timeout}')
        element = WebDriverWait(self.driver, timeout).until(
            lambda x: x.find_element(*locator))
        return element

    def back(self, num=1):
        logging.info(f'back:{num}')
        for i in range(num):
            self.driver.back()
