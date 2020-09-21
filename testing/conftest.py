import pytest


@pytest.fixture(autouse=True)
def login(request):
    print("登录方法根目录")
    # print(request.param)
    # yield生成器 激活fixture teardown方法，相当于return，并且记住上一次的执行
    yield ['username', 'password']
    print('teaedown')
