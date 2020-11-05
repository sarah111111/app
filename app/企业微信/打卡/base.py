import pytest

from appium import webdriver


class Base:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'com.tencent.wework'  # 包名
        desired_caps['appActivity'] = '.launch.WwMainActivity'  # 页面名
        desired_caps['noReset'] = 'true'  # 测试前后是否重置环境（如首次打开弹框，或者登录信息）
        # desired_caps['dontStopAppOnReset']='true' #首次启动的时候，不停止app
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过安装，权限设置等操作
        desired_caps['unicodeKeyboard'] = 'true'  # 是否需要输入非英文之外的语音并在测试完成后重置输入法
        desired_caps['resetKeyBoard'] = 'true'
        desired_caps['dontStopAppOnReset'] = 'true'
        desired_caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(50)

    def teardown(self):
        self.driver.quit()
