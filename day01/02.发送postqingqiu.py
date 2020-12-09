import requests

...
# 发送post请求
...
# 登录的接口
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/login"
user = {
    "mobilephonr": "18793254688",
    "pwd": "123456"
}
# 用data传表单参数，content-type:application/x-www-from-urlencoded
r = requests.post(url, data=user)
print(r.text)

#
url = "http://www.httpbin.org/post"
user = {
    "mobilephonr": "18793254688",
    "pwd": "123456"
}
r = requests.post(url, data=user)
print(r.text)
print("*" * 50)  # 分割线
# 用json传参数，content-type：application/json
r = requests.post(url, json=user)
print(r.text)

# 练习：充值接口，给注册用户充值
url = "http://192.168.150.54:8089/futureloan/mvc/api/member/recharge"
user = {
    "mobilephone": "18793254688",
    "amount": "1000"
}
# 使用data还是json传参，要看接口实现的是哪个
r = requests.post(url, data=user)
print(r.text)
assert r.json()['status'] == 1
assert r.json()['data']['regname'] == "Hello"
assert r.json()['data']['mobilephone'] == "18793254688"
print(r.json()['data']['leaveamount'])
