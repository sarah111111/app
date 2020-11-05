"""
添加人员页面
"""
# from app.企业微信.page.addmeberpage import AddMeberPage
from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app.企业微信.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    name_element = (MobileBy.XPATH, "//*[contains(@text,'必填')]")
    gender_element = (MobileBy.XPATH, "//*[@text='男']")
    male_ele = (MobileBy.XPATH, "//*[@text='男']")
    female = (MobileBy.XPATH, "//*[@text='女']")
    phonenum_element = (MobileBy.ID, "com.tencent.wework:id/fiv")
    save_element = (MobileBy.ID, "com.tencent.wework:id/hxt")

    def set_name(self, name):
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'必填')]").send_keys(name)
        self.find_and_sendkeys(self.name_element, name)
        return self

    def set_gander(self, gender):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.find_and_click(self.gender_element)
        sleep(5)
        if gender == "男":
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            self.find_and_click(self.male_ele)
        else:
            # self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click(self.female)
        return self

    def set_phonenum(self, phonenum):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/fiv").send_keys(phonenum)
        self.find_and_sendkeys(self.phonenum_element, phonenum)
        return self

    def click_save(self):
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hxt").click()
        self.find_and_click(self.save_element)
        from app.企业微信.page.addmeberpage import AddMeberPage
        return AddMeberPage(self.driver)
