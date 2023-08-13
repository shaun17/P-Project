import requests

# 获取热门汇率列表信息
toppic = ('https://www.mxnzp.com/api/exchange_rate/list?&app_id=iyrfporilxichdhf&app_secret'
          '=0WOWsk0WZ27Mc2ksGoR74eeR3WE9O8Y6')

# 查看指定货币编号的汇率信息
url = ('https://www.mxnzp.com/api/exchange_rate/aim?from=USD&to=CNY&app_id=iyrfporilxichdhf&app_secret'
       '=0WOWsk0WZ27Mc2ksGoR74eeR3WE9O8Y6')

params = {"app_id": "iyrfporilxichdhf",
          "app_secret": "0WOWsk0WZ27Mc2ksGoR74eeR3WE9O8Y6",
          "from": "USD",
          "to": "CNY"}


# 获取支持的货币编号列表
def get_config_url(pa):
    return ('https://www.mxnzp.com/api/exchange_rate/configs?'
            'app_id=' + pa["app_id"] +
            '&app_secret=' + pa["app_secret"])


# 查看指定货币编号的汇率信息
def get_url(pa):
    return ('https://www.mxnzp.com/api/exchange_rate/aim?'
            'from=' + pa["from"] +
            '&to=' + pa["to"] +
            '&app_id=' + pa['app_id'] +
            '&app_secret=' + pa['app_secret'])


def exchange_rate_configs(from_current):
    params["from"] = from_current
    response = requests.get(get_url(params))
    response_dict = response.json()
    return response_dict.get("data").get("price")


