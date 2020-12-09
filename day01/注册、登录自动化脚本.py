...
# 线性脚本实现，完成注册、登录两个接口的自动化脚本
...

import requests

# # 注册
# url1 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone": "18793254634",
#     "pwd": "123456",
# }
# r = requests.get(url1, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == '10001'
# assert r['msg'] == '注册成功'
#
# url2 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone": "18793254635",
#     "pwd": "123456789123456789",
# }
# r = requests.get(url2, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == '10001'
# assert r['msg'] == '注册成功'
#
# url3 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone": "18793254636",
#     "pwd": "123456",
#     "regname":"闪电"
# }
# r = requests.get(url3, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == '10001'
# assert r['msg'] == '注册成功'
#
# url4 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
# user = {
#     "mobilephone": "18793254637",
#     "pwd": "123456",
#     "regname":"闪电"
# }
# r = requests.get(url4, params=user)
# r = r.json()
# print(r)
# assert r['status'] == 1
# assert r['code'] == '10001'
# assert r['msg'] == '注册成功'

url5 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": None,
    "pwd": "123456",
}
r = requests.get(url5, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '手机号不能为空'

url6 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": None,
    "pwd": "123456",
    "regname":"闪电"
}
r = requests.get(url6, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '手机号不能为空'

url7 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "165432",
    "pwd": "123456",
}
r = requests.get(url7, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url8 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "165432",
    "pwd": "123456",
    "regname":"闪电"
}
r = requests.get(url8, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url9 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "123456789123",
    "pwd": "123456",
}
r = requests.get(url9, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url10 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "123456789123",
    "pwd": "123456",
    "regname":"闪电"
}
r = requests.get(url10, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url11 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "123abcd765f",
    "pwd": "123456",
    "regname":None
}
r = requests.get(url11, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url12 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "123abcd891f",
    "pwd": "123456",
    "regname":"闪电"
}
r = requests.get(url12, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url13 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "这是手机号",
    "pwd": "123456",
    "regname":None
}
r = requests.get(url13, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url14 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "这是手机号",
    "pwd": "123456",
    "regname":"闪电"
}
r = requests.get(url14, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url15 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "11111111111",
    "pwd": "123456",
    "regname":"闪电"
}
r = requests.get(url15, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url16 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "111111111111",
    "pwd": "123456",
    "regname":None
}
r = requests.get(url16, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20109'
assert r['msg'] == '手机号码格式不正确'

url17 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13567890987",
    "pwd": "123",
    "regname":"闪电"
}
r = requests.get(url17, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20108'
assert r['msg'] == '密码长度必须为6~18'

url18 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13567890987",
    "pwd": "123",
    "regname":None
}
r = requests.get(url18, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20108'
assert r['msg'] == '密码长度必须为6~18'

url19 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13567890987",
    "pwd": "123456789123456789123456789",
    "regname":None
}
r = requests.get(url19, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20108'
assert r['msg'] == '密码长度必须为6~18'

url20 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13567890987",
    "pwd": "123456789123456789123456789",
    "regname":"闪电"
}
r = requests.get(url20, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20108'
assert r['msg'] == '密码长度必须为6~18'

url21 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13567890987",
    "pwd": None,
    "regname":"闪电"
}
r = requests.get(url21, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '密码不能为空'

url22 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13567890987",
    "pwd": None,
    "regname":None
}
r = requests.get(url22, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '密码不能为空'

url23 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13567890987",
    "pwd": "123456",
    "regname":None
}
r = requests.get(url23, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20110'
assert r['msg'] == '手机号码已被注册'

url24 = "http://192.168.150.54:8089/futureloan/mvc/api/member/register"
user = {
    "mobilephone": "13567890987",
    "pwd": "123",
    "regname":"闪电"
}
r = requests.get(url24, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20108'
assert r['msg'] == '密码长度必须为6~18'

# 登录
url25 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "13567890987",
    "pwd": "123456",
    "regname":"闪电"
}
r = requests.get(url25, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20110'
assert r['msg'] == '成功'

url26 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "13567890987",
    "pwd": "123456",
}
r = requests.get(url26, params=user)
r = r.json()
print(r)
assert r['status'] == 1
assert r['code'] == '10001'
assert r['msg'] == '登录成功'

url27 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": None,
    "pwd": "123456789123456789",
}
r = requests.get(url27, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '手机号不能为空'

url28 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": None,
    "pwd": "135456",
}
r = requests.get(url28, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '手机号不能为空'

url29 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "135456789123456",
    "pwd": "135456",
}
r = requests.get(url29, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或者密码错误'

url30 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "13567890981",
    "pwd": "135456",
}
r = requests.get(url30, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或者密码错误'

url31 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "13567890982",
    "pwd": None,
}
r = requests.get(url31, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20103'
assert r['msg'] == '参数错误:参数不能为空'

url32 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "13567890981",
    "pwd": "135",
}
r = requests.get(url32, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或者密码错误'

url33 = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephone": "13567890981",
    "pwd": "135456789123456789123456789",
}
r = requests.get(url33, params=user)
r = r.json()
print(r)
assert r['status'] == 0
assert r['code'] == '20111'
assert r['msg'] == '用户名或者密码错误'



















