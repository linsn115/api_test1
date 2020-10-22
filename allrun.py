from requets_url import get_token
from requets_url import handlerequests
from requets_url import logutil2
from requets_url import read_excel
import json

loger = logutil2.Logs()
re = read_excel.ReadExcel()
mt = handlerequests.HandleRequests()
data_list = re.excel_to_list("D://python//api_test//data//url.xlsx","Sheet1")
print(data_list)
# case_data = re.get_test_data(data_list,"test_login")
# print(case_data)

for case_data in data_list:

    headers = case_data['headers']
    print(type(headers))
    method = case_data['method']
    url = case_data['url']
    data = case_data['data']
    print(method)
    if method == "POST":
        print("method is post")
        if headers == '':
            res = mt.post(url=url, data=data)
            mt.post_res(res)
            #res = requests.post(url=case['url'], data=case['data'])
        else:
            if "blade-auth" in json.loads(headers).keys():
                print("token is ")
                headers = json.loads(headers)
                token = get_token.get_token()
                print("token:%s" % token)
                print(type(token))

                headers["blade-auth"] = "bearer " + get_token.get_token()
                print(headers["blade-auth"])
                res = mt.post(url=url, headers=headers, json=data)
                mt.post_res(res)
            else:
                res =  mt.post(url=url, json=data , headers=json.loads(headers))
                mt.post_res(res)
                staus_code = res.status_code
                print("status_code:%s"%staus_code)
                print("res.text:%s"%res.text)
    else:
        res = mt.get(url=url,params=data)
        mt.get_res(res)