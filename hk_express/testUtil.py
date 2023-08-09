import hashlib
import time
import requests
import datetime


def get_md5():
    strs = str(int(time.time()))
    hl = hashlib.md5()
    hl.update(strs.encode(encoding='utf-8'))
    print("mds:" + hl.hexdigest())


def get_date(start_str, end_str):
    start = datetime.datetime.strptime(start_str, '%Y-%m-%d')
    end = datetime.datetime.strptime(end_str, '%Y-%m-%d')

    delta = end - start

    dates = []
    for i in range(delta.days + 1):
        day = start + datetime.timedelta(days=i)
        dates.append(day.strftime('%Y-%m-%d'))
    return dates


def get_url():
    params = {"SearchType": "ONEWAY",
              "OriginStation": "HKG",
              "DestinationStation": "ICN",
              "DepartureDate": "5/9/2023"}
    url = ("https://booking.hkexpress.com/zh-cn/select/?SearchType=" +
           params.get("SearchType") + "&OriginStation=" +
           params.get("OriginStation") + "&DestinationStation=" +
           params.get("DestinationStation") + "&DepartureDate=" +
           params.get("DepartureDate") + "&Adults=1&rediscoverbooking=false&")
    print(url)


def request_by_url():
    token = "7dd545716c795c4f306b06ace901bbb2"
    url = "https://availability-api.hkexpress.com/api/v1.0/availability/dayavailability?token=" + token + "&outboundDate=2023-09-05"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'Apikey': 'd9eaa63c9008987381860a36e0d8c2aa2c6a936b41bf35e42bbe11e97bd452ea'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.text)
    else:
        print("请求失败", response.text)
