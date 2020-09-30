import requests
import time
import re
import json


def get_auth_token(url,user,password,hearders):
    se = requests.session()
    null = None

    req_data = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "user": user,
            "password": password
        },
        "id": 1,
        "auth": null
    }

    content = se.post(url,data=json.dumps(req_data),headers=headers).text
    # print(req_data)
    # print(json.dumps(req_data))
    # print(json.loads(content))
    # print(json.loads(content)['result'])
    return json.loads(content)['result']

def get_user(url,token,hearders):
    se = requests.session()
    req_data = {
        "jsonrpc": "2.0",
        "method": "user.get",
        "params": {
            "output": "extend"
        },
        "auth": token,
        "id": 1
    }
    content = se.post(url,data=json.dumps(req_data),headers=headers).text
    return json.loads(content)

if __name__ == "__main__":
    url = "https://zabbix.hgymall.com/zabbix/api_jsonrpc.php"
    user = "Admin"
    password = "zabbix"
    headers = {'Content-Type': 'application/json-rpc'}
    token = get_auth_token(url,user,password,headers)
    print(token)

    print(get_user(url,token,headers))