"""
存放 app应用常用的一些方法：比如启动app,关闭app,停止app,进入首页
"""
from appium import webdriver

from app.企业微信po.page.basepage import BasePage
from app.企业微信po.page.mainpage import MainPage


class App(BasePage):

    def start(self):
        """
        启动app
        :return:
        """
        if self.driver == None:
            # 第一次调用start方法的时候driver为None
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
        else:
            # launch_app()这个方法不需要传入任何参数，会自动启动起来desirecapa里面定义的activity
            # start_activity(packagename,activityname) 可以启动其它的应用的页面
            self.driver.launch_app()
        self.driver.implicitly_wait(50)
        return self  # return到自己

    def restart(self):
        """
        重启app
        :return:
        """
        self.driver.close()
        self.driver.launch_app()
        return self

    def stop(self):
        """
        停止app
        :return:
        """
        self.driver.quit()

    def goto_main(self):
        """
        进入首页
        :return:
        """
        return MainPage(self.driver)  # MainPage页需要的driver
