"""
添加人员
"""
# from app.企业微信.page.contactAddPage import ContactAddPage
from appium.webdriver.common.mobileby import MobileBy

from app.企业微信po.page.basepage import BasePage


class AddMeberPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver
    add_manual_element = (MobileBy.XPATH, "//*[@text='手动输入添加']")
    toast_element = (MobileBy.XPATH, "//*[@class='android.widget.Toast']")

    def add_meual(self):
        """
        手动输入添加
        :return:
        """
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.find_and_click(self.add_manual_element)  # 改造后
        from app.企业微信po.page import ContactAddPage
        return ContactAddPage(self.driver)

    def get_toast(self):
        # 判断是否添加成功 TOAST
        # self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']")
        # element = WebDriverWait(self.driver, 10).until(
        #     lambda x: x.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']"))
        element = self.webderiver_wait(self.toast_element)
        result = element.text
        # text = '成功'
        return result
