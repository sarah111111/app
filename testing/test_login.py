import pytest


# 测试用例执行前先执行login方法
def test_case1(login):
    print(f"case1 login ={login} ")


def test_case2():
    print("case2")


def test_case3():
    print("case3")
