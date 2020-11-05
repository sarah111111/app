"""
通讯录列表页
"""
from appium.webdriver.common.mobileby import MobileBy

from app.企业微信.page.addmeberpage import AddMeberPage
from app.企业微信.page.basepage import BasePage


class ContactListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    addmember_text = "添加成员"

    def add_contact(self):
        """
        添加成员
        :return:
        """
        addmember_text = "添加成员"
        # 点击添加成员
        # self.driver.find_element(
        #     MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
        #                                   '(new UiSelector().'
        #                                   'scrollable(true).'
        #                                   'instance(0)).'
        #                                   'scrollIntoView('
        #                                   'new UiSelector().'
        #                                   'text("添加成员").instance(0));').click()
        self.find_by_scroll(self.addmember_text).click()  # 改造后
        return AddMeberPage(self.driver)

    def search_contact(self):
        """
        搜索人员
        :return:
        """
        pass
