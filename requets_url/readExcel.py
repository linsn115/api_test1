import xlrd
import requests
import json
from requets_url import get_token
import logutil2

import logging
#logger = logging.getLogger(__name__)
wb = xlrd.open_workbook("..//data//url.xlsx")

sh =wb.sheet_by_name("Sheet1")

print(sh)
print(sh.nrows)
print(sh.ncols)
logger = logutil2.logs()
logger.info("this is info")
# cell = sh.row_values(1)
# res = requests.post(url=cell[2], headers=json.loads(cell[4]), data=json.loads(cell[5]))
# print(res.text)
# for i in range(sh.nrows):
#     print(sh.row_values(i))
#     cell = sh.row_values(i)
    #res = requests.post(url=cell(2), headers=cell(4), data=cell(5))
for i in range(1,sh.nrows):
    print(sh.row_values(i))
    cell = sh.row_values(i)
    headers = cell[4]
    method = cell[3]
    if method =="POST":
        if headers == '':
            res = requests.post(url=cell[2], data=cell[5])
        else:
            if  "blade-auth" in headers:
                headers = json.loads(headers)
                token = get_token.get_token()
                print("token:%s"%token)
                print(type(token))

                headers["blade-auth"]="bearer " + get_token.get_token()
                print(headers["blade-auth"])
                res = requests.post(url=cell[2], headers=headers, data=cell[5])
            else:
                res = requests.post(url=cell[2], headers=json.loads(headers), data=cell[5])
    else:
        if headers == '':
            res = requests.get(url=cell[2], data=cell[5])
        else:
            if  "blade-auth" in headers:
                headers = json.loads(headers)
                token = get_token.get_token()
                print("token:%s"%token)
                print(type(token))
                print(headers["blade-auth"])
                headers["blade-auth"]="bearer " + get_token.get_token()
                print(headers)
                res = requests.get(url=cell[2], headers=headers)

            else:
                res = requests.get(url=cell[2], headers=json.loads(headers), data=cell[5])
    print(res.text)