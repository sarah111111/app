from time import sleep

from appium.webdriver.common.mobileby import MobileBy

from app.企业微信.打卡.base import Base


class TestDaka(Base):

    def test_daka(self):
        # 步骤1：点击工作台
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        # 步骤2：滚动查找 "打卡" 元素
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("打卡").instance(0));').click()
        sleep(5)
        # 步骤3：点击"打卡"
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/att").click()
