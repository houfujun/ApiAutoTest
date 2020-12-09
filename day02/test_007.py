'''
fixture带参数
'''
import pytest


# 测试数据
# 参数使用params关键词，一个列表，列表中有5组数据，前三组数据是字典
import requests


@pytest.fixture(params=[{"username": "root", "pwd": "123456"},
                        {"username": "admin", "pwd": "888888"},
                        {"username": "administrator", "pwd": "Hellopwd"},
                        "four",
                        5])
def login_data(request):  # 参数request是固定的，不能写成其他
    return request.param  # 使用request.param返回每组数据


# 测试逻辑（测试步骤）
# 登录功能的测试脚本
def test_login(login_data):
    print(f"测试登陆功能，测试数据为:{login_data}")


# 注册接口的测试代码
@pytest.fixture(params=[
    {"data": {"mobilephone": "18045324567", "pwd": "123456"},
     "expect": {"msg": "手机号码已被注册", "code": "21110"}},
    {"data": {"mobilephone": "18045324568", "pwd": "123"},
     "expect": {"msg": "密码长度必须为6~18", "code": "20108"}},
    {"data": {"mobilephone": "18045324569", "pwd": "1234567891234567890123456789"},
     "expect": {"msg": "密码长度必须为6~18", "code": "20108"}},
])
def register_data(request):
    return request.param


def test_register(register_data):
    url = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
    print("测试数据", register_data['data'])
    print("预期结果", register_data['expect'])
    r = requests.post(url, data=register_data['data'])
    print(r.text)
    assert r.json()['msg'] == register_data['expect']['msg']
