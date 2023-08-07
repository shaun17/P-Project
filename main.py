# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import requests;

headers = {"Host": "app.dewu.com",
           "appId": "h5",
           "appVersion": "5.12.1",
           "duToken": "d41d8cd9|11452803|1677769006|84d20e8e7eac47aa",
           "Accept": "application/json, text/plain, */*",
           "Accept-Language": "zh-CN,zh-Hans;q=0.9",
           "Accept-Encoding": "gzip, deflate, br",
           "Content-Type": "application/json",
           "Origin": "http://m.dewu.com",
           "Content-Length": "16",
           "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/duapp/5.12.1",
           "Referer": "http://m.dewu.com/",
           "cookieToken": "d41d8cd9|11452803|1677769006|84d20e8e7eac47aa",
           "Cookie": "duToken=d41d8cd9|11452803|1677769006|84d20e8e7eac47aa; x-auth-token=Bearer eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2Nzc3NjkwMDYsImV4cCI6MTcwOTMwNTAwNiwiaXNzIjoiVVVJRDlkYmRjZjZhODQwZTRhZWFhM2IxZmRiZDMzNDdhZWJhIiwic3ViIjoiVVVJRDlkYmRjZjZhODQwZTRhZWFhM2IxZmRiZDMzNDdhZWJhIiwidXVpZCI6IlVVSUQ5ZGJkY2Y2YTg0MGU0YWVhYTNiMWZkYmQzMzQ3YWViYSIsInVzZXJJZCI6MTE0NTI4MDMsImlzR3Vlc3QiOmZhbHNlfQ.eilpIsLjciewBSYbFb_LQvBtKLun9dRK81nT_QW7PTUmu_N-C9_ctX8Y182Iz24kiV5XljrXq7ba5xj1yL1rj3fZ_AEFJXe4N_X0-YGuri14hot7XcE3z-dkhCE1-q243K5hlLq6Hie1NXpMqwvjmrcXl31E7ZHbE1Ycc0FWWdSXbJTpzF32tnEwXlv0lPPSww6TbmzhYhdowdJNaMH9q7istVKhnzeOhHODFCaDwbIsKFX8rb5NWhg65xpT7Kcup7CyZju5wddmzwyD4wQe4BPJnJ5Nu28p8hkFf4hEu-uEE99N3_EDttiDe6AK6zYyevxOVg-pMB9n75_beSbC_Q",
           "x-auth-token": "Bearer eyJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2Nzc3NjkwMDYsImV4cCI6MTcwOTMwNTAwNiwiaXNzIjoiVVVJRDlkYmRjZjZhODQwZTRhZWFhM2IxZmRiZDMzNDdhZWJhIiwic3ViIjoiVVVJRDlkYmRjZjZhODQwZTRhZWFhM2IxZmRiZDMzNDdhZWJhIiwidXVpZCI6IlVVSUQ5ZGJkY2Y2YTg0MGU0YWVhYTNiMWZkYmQzMzQ3YWViYSIsInVzZXJJZCI6MTE0NTI4MDMsImlzR3Vlc3QiOmZhbHNlfQ.eilpIsLjciewBSYbFb_LQvBtKLun9dRK81nT_QW7PTUmu_N - C9_ctX8Y182Iz24kiV5XljrXq7ba5xj1yL1rj3fZ_AEFJXe4N_X0 - YGuri14hot7XcE3z - dkhCE1 - q243K5hlLq6Hie1NXpMqwvjmrcXl31E7ZHbE1Ycc0FWWdSXbJTpzF32tnEwXlv0lPPSww6TbmzhYhdowdJNaMH9q7istVKhnzeOhHODFCaDwbIsKFX8rb5NWhg65xpT7Kcup7CyZju5wddmzwyD4wQe4BPJnJ5Nu28p8hkFf4hEu - uEE99N3_EDttiDe6AK6zYyevxOVg - pMB9n75_beSbC_Q",
           "Connection": "keep-alive"
           }

def print_coupon():
    url = "https://app.dewu.com/api/v1/h5/nine-tails/newbie/coupons/querySpuWaterfallTab?sign=60e885beb0f2c7752e89eed15c493424"
    raw = {"sourceType": 0}
    r = requests.post(url=url, headers=headers, json=raw)
    print(r.text)


def print_coupon2():
    url = "https://app.dewu.com/api/v1/h5/nine-tails/newbie/coupons/config?sign=0568b556efc69fa8933a5f06989c30f6"
    raw = {"sorceFrom": 0, "advAbType": 2, "advSpuPriceAb": 2, "limitTaskAb": 2, "zeroLotteryAb": ''}
    r = requests.post(url=url, headers=headers, json=raw)
    print(r.text)

def session_coupon():
    s = requests.Session



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_coupon()
    print_coupon2()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
