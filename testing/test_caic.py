# 被测文件
import pytest

# from pythoncode.caic import Calclator

import sys

import yaml

print(sys.path.append('..'))
from pythoncode.caic import Calclator


def setup_module():
    print("模块级别 setup")


def teardown_module():
    print("模块级别 teardown")


# 函数级别 类外面的使用def 定义的叫函数
# 在类里面使用def 定义的叫方法
def setup_function():
    print("函数级别 setup")


def teardown_function():
    print("函数级别 teardown")


with open("datas/caic.yml") as f:
    datas = yaml.safe_load(f)
    mydis = datas.keys()
    mydatas = datas.values()


class TestCalc:
    # 每个类里面 前和后分布执行 setup_class teardown_class
    def setup_class(self):
        print("类级别 setup")

    def teardown_class(self):
        print("类级别 teardown")

    # 每条类里面的测试用例前和后分布执行 setup teardown
    def setup(self):
        self.cal = Calclator()
        print("setup")

    def teardown(self):
        print("teardown")

    @pytest.mark.add
    @pytest.mark.parametrize('a, b, result', mydatas
        , ids=mydis)
    def test_add(self, a, b, result):
        # cal = Calclator()
        assert result == self.cal.add(a, b)
        assert result == self.cal.add(a, b)
        assert result == self.cal.add(a, b)

    @pytest.mark.add
    def test_add1(self):
        # cal = Calclator()
        assert 3 == self.cal.add(1, 2)

    @pytest.mark.div
    def test_div(self):
        # cal = Calclator()
        assert 1 == self.cal.div(1, 1)

    def test_assume(self):
        print("登录操作")
        pytest.assume(1 == 2)
        print("搜索操作")
        pytest.assume(2 == 2)
        print("加购操作")
        pytest.assume(3 == 2)
