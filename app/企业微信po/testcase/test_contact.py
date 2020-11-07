# 页面逻辑不变的情况下，这里面的内容一般不变
import pytest
import yaml

from app.企业微信po.page.app import App

# 运行提示gbk时要加入“rb”参数
with open("../datas/addcontact.yml", 'rb') as f:
    addcontactdatas = yaml.safe_load(f)


class TestContact:

    def setup_class(self):
        self.app = App()  # 创建一个app实例
        self.main = self.app.start().goto_main()  # 调用app的方法

    def teardown_class(self):
        self.app.stop()

    @pytest.mark.parametrize('name,gender,phonenum',
                             addcontactdatas
                             )
    def test_addcontact(self, name, gender, phonenum):
        """
        添加联系人
        :return:
        """
        # name = "po2"
        # gander = "女"
        # phonenum = "18310771112"
        mypage = self.main.goto_contactlist(). \
            add_contact().add_meual(). \
            set_name(name). \
            set_gander(gender). \
            set_phonenum(phonenum). \
            click_save()
        text = mypage.get_toast()
        assert '成功' in text
        self.app.back()
