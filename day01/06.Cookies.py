'''
Cookie:
http协议：无状态、无连接、媒体独立
每个请求都是独立的，有一些借口登录后才能访问，需要使用Cookies验证用户是否登录
account/dashboard 用户没有登录时，返回登录的页面
account/dashboard 如果登录了，返回用户的详细信息。浏览器登录后，获取到的cookie直接放到自动化来用
如果cookie失败或者换其他用户登录，就不能继续访问了
'''
import requests

# 百格网站，有一些接口登录之后才能访问
print("未登录时，返回结果为:")
url = "https://www.bagevent.com/account/dashboard"
r = requests.get(url)
print(r.text)

# 用Fidder抓到的包，将里面的头设置在这里
head = {
    "Cookie":'__auc=5016c91d17627483bb77f2ccd63;MEIQIA_TRACK_ID=1l8Rcrkd9w7Lr30RnkxrLO0ZBt6;MEIQIA_VISIT_ID=1l8RcrqRDATROk2XfTQDteTZsMs;_ga=GA1.2.1550708338.1606976824;BAG_EVENT_TOKEN_=02de735f68204d51009e7edda78e58c13a3fcdd1;BAG_EVENT_CK_KEY_="2780487875@qq.com";BAG_EVENT_CK_TOKEN_=2440f5d17af838308ba4b390db81af38;JSESSIONID=4A45C38EC89CB49CCA52D99FFE4A1845;BAGSESSIONID=1fab0fa8-71f1-4bf4-91e0-01eff2bf4ff7;__asc=08e62c5f1762cbf92c556dd7a25;_gid=GA1.2.2029278637.1607068521;Hm_lvt_1fc37bec18db735c69ebe77d923b3ab9=1606976813,1607068521;_gat=1;Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1607070990'
}
print("登录后，返回的结果为：")
r = requests.get(url, headers=head)
print(r.text)
