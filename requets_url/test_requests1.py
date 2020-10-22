import requests
import json
# url = "http://192.168.2.73:999/blade-auth/token"  # 参数可以写到url里
# res = requests.get(url=url) # 第一个url指get方法的参数，第二个url指上一行我们定义的接口地址
# print(res.text)

url = "http://192.168.2.73:999/blade-auth/token"
header = {"Accept": "application/json",
          "Authorization": "Basic YW5jaG9yOmFuY2hvcl9zZWNyZXQ=",
          "User-Type": "KH"}
data = {
    "account": "admin",
    "password": "123456",
    "grantType": "password"
}  # 多行文本, 字符串格式，也可以单行（注意外层有引号，为字符串） data = '{"name": "hanzhichao", "age": 18}'
res = requests.post(url=url, headers=header, data=data)  # data支持字典或字符串
print(res.text)
resonse = json.loads(res.text)
print(resonse)
token = resonse["data"]["accessToken"]
print(token)


print("code:%s"%res.status_code)
print("reason:%s"%res.reason)

print("encoding:%s"%res.encoding)
print("json:%s"%res.json())
print("headers:%s"%res.headers)
print("cookie:%s"%res.cookies)