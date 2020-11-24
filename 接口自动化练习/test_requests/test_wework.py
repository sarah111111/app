import json
import random
import re

import pytest
import requests


def test_data():
    "userid, name, mobile"
    # data = [(str(random.randint(0, 9999999)),
    #          "柯南",
    #          str(random.randint(13800000000, 13899900000))) for x in range(3)]
    data = [("kenanxx" + str(x),
             "柯南",
             "138%08d" % x) for x in range(20)]  # %x替换到%d
    print(data)
    return data


class TestWework:
    @pytest.fixture(scope="session")
    def token(self):
        """
        创建静态的token
        :return:
        """
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2fb4dce2efc1ecb9&corpsecret=YFKp8ZStHAX71LyzTgbLMXkah-0ZzWjKaJTHToTBPAQ",
            verify=False)
        # print(r.json()['access_token'])  # 提取tookin
        return r.json()['access_token']

    def get_token(self):

        """
        获取token
        https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ID&corpsecret=SECRET
        :return:
        """
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww2fb4dce2efc1ecb9&corpsecret=YFKp8ZStHAX71LyzTgbLMXkah-0ZzWjKaJTHToTBPAQ",
            verify=False)
        # print(r.text)
        # print(type(r))
        # print(r.json()['access_token'])  # 提取tookin
        return r.json()['access_token']

    def test_create_user(self, token, userid, mobile, name="柯南", department=None):
        """
        创建成员
        https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN
        :return:
        """
        # access_token =self.get_token() #将上面方法获取的token传过来
        if department is None:
            department = [1]
        request_body = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}", json=request_body,
                          verify=False)
        return r.json()

    def test_get_user(self, token, userid):
        """
        获取成员信息
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}",
                         verify=False)
        # print(r.json())
        return r.json()

    def test_update_user(self, token, userid, name="柯南"):
        """
        更新成员信息
        :return:
        """
        requests_body = {
            "userid": userid,
            "name": name
        }
        r = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}", json=requests_body,
                          verify=False)
        # print(r.json())
        return r.json()

    def test_delete_user(self, token, userid):
        """
        删除成员信息
        :return:
        """
        r = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}",
                         verify=False)
        return r.json()

    @pytest.mark.parametrize("userid, name, mobile", test_data())
    def test_wework(self, token, userid, name, mobile):
        """
        整体测试
        :return:
        """
        try:
            assert "created" == self.test_create_user(token, userid, mobile)["errmsg"]
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid = re.findll(":(.*)'$", e.__str__())[0]  # print(e)=e.__str__
                self.test_delete_user(token, re_userid)
                assert "created" == self.test_create_user(token, userid, mobile)["errmsg"]
        assert name == self.test_get_user(token, userid)["name"]
        assert "updated" == self.test_update_user(token, userid, name="柯南5555")["errmsg"]
        assert "柯南5555" == self.test_get_user(token, userid)["name"]
        assert "deleted" == self.test_delete_user(token, userid)["errmsg"]
        assert 60111 == self.test_get_user(token, userid)["errcode"]
