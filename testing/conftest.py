from typing import List

import pytest
import yaml


@pytest.fixture(autouse=True)
def login(request):
    print("登录方法根目录")
    # print(request.param)
    # yield生成器 激活fixture teardown方法，相当于return，并且记住上一次的执行
    yield ['username', 'password']
    print('teaedown')


def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    print(items)
    print(len(items))
    items.reverse()  # 用例倒序执行倒序
    # 修改yml数据的标签为汉字
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# 命令行去添加一个参数
def pytest_addoption(parser):
    mygroup = parser.getgroup("hogwarts")  # group 将下面所有的 option都展示在这个group下。
    mygroup.addoption("--env",  # 注册一个命令行选项
                      default='test',
                      dest='env',
                      help='set your run env'
                      )


@pytest.fixture(scope='session')
def cmdoption(request):
    myenv = request.config.getoption("--env", default='test')
    if myenv == 'test':
        datapath = 'datas/test/data.yml'
    if myenv == 'dev':
        datapath = 'datas/dev/data.yml'

    with open(datapath) as f:
        datas = yaml.safe_load(f)

    return myenv, datas


# 通过方法动态的生成测试用例
def pytest_generate_tests(metafunc: "Metafunc") -> None:
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.mydatas,
                             ids=metafunc.module.myids,
                             scope='function')
