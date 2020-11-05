"""
首页主页面
"""
from appium.webdriver.common.mobileby import MobileBy

from app.企业微信.page.basepage import BasePage
from app.企业微信.page.contactlistPage import ContactListPage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver 在基类里面封装，
    contactlist = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactlist(self):
        """
        进入到通讯录
        :return:
        """
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.find_and_click(self.contactlist)  # 改造后
        return ContactListPage(self.driver)

    def goto_workbench(self):
        """
        进入到打卡
        :return:
        """
        pass
