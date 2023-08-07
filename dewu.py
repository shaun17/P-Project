import requests
import execjs
import json
import warnings
import logging

warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s:%(message)s')

with open("sign.js", 'r', encoding="utf-8") as f:
    ctx = execjs.compile(f.read())


def getData(page):
    url = "https://app.dewu.com/api/v1/h5/index/fire/shopping-tab"

    headers = {
        "你的headers"
    }
    if page == 0:
        firstParams = {"tabId": 1000008, "limit": 20, "lastId": ""}
        sign = ctx.call("getSign", firstParams)
        secondParams = {"sign": sign, "tabId": 1000008, "limit": 20, "lastId": ""}
    else:
        firstParams = {"tabId": 1000008, "limit": 20, "lastId": f"{page}"}
        sign = ctx.call("getSign", firstParams)
        secondParams = {"sign": sign, "tabId": 1000008, "limit": 20, "lastId": f"{page}"}
    resq = requests.post(url, headers=headers, data=json.dumps(secondParams), verify=False)
    data = resq.json()["data"]["list"]
    resultList = []
    for da in data:
        articleNumbers = da["product"].get("articleNumbers")
        articleNumbers = articleNumbers[0] if articleNumbers else ""
        sellDate = da["product"].get("sellDate")
        sellDate = sellDate if sellDate else ""

        result = {
            "spuId": da["product"]["spuId"],
            "title": da["product"]["title"],
            "price": da["product"]["price"],
            "sourceName": da["product"]["sourceName"],
            "articleNumber": da["product"]["articleNumber"],
            "articleNumbers": articleNumbers,
            "recommendRequestId": da["product"]["recommendRequestId"],
            "sellDate": sellDate,
            "categoryId": da["product"]["categoryId"],
            "soldCountText": da["product"]["soldCountText"]

        }
        resultList.append(result)

    return resultList


def run():
    for page in range(2):
        logging.info(f"获取第{page + 1}页")
        resultList = getData(page)
        logging.info("获取的数据：%s", resultList)


if __name__ == '__main__':
    run()
