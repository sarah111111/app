#
# datas = [1,2,3],[0.2,0.3,0.4]
# myids = ['整数',"浮点数"]
import yaml

with open('datas/test/a.yml') as f:
    datas = yaml.safe_load(f)
    myids = datas.keys()
    mydatas = datas.values()


def test_param(param):
    print(f"param= {param}")
    print("动态生成测试用例")
