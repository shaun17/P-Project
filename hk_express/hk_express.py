from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import testUtil
import logging

from utils.hk_express_util import get_schedules, date_formate_conv


def get_url(pa):
    return ("https://booking.hkexpress.com/zh-cn/select/?SearchType=" +
            pa.get("SearchType") + "&OriginStation=" +
            pa.get("OriginStation") + "&DestinationStation=" +
            pa.get("DestinationStation") + "&DepartureDate=" +
            pa.get("DepartureDate") + "&Adults=1&rediscoverbooking=false&")


def script(original_url, wait_times, flight_date):
    browser = webdriver.Chrome()
    browser.get(original_url)  # 访问网页

    # 延迟wait_times 秒
    wait = WebDriverWait(browser, wait_times)
    # 定位到flightselect_header 标签，也就是航班时刻表
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'flightselect_header')))

    # cookies = browser.get_cookies()
    # print(type(cookies), cookies)  # 获取cookies,格式：<class 'list'>
    # SC = browser.page_source
    # print(type(SC), SC)

    flights = browser.find_elements(By.CLASS_NAME, 'rowFlight')
    for f in flights:
        # each_schedule = f.find_element(By.CLASS_NAME, "custom-adjust-label-position")
        get_schedules(f, flight_date)
        print("----------------------------------------------------------------------")


params = {"SearchType": "ONEWAY",
          "OriginStation": "HKG",
          "DestinationStation": "ICN",
          "DepartureDate": "5/9/2023"}


def positive_or_negative(new_date, new_params):
    for x in new_date:
        times = 20
        datestr = date_formate_conv(x)
        new_params["DepartureDate"] = datestr
        url = get_url(new_params)
        print(url)
        # 超时放大等待响应时间，再舱室两次
        try:
            script(url, times, x)
        except Exception as e:
            while times <= 30:
                logging.error(e)
                times = times + 5
                script(url, times, x)
            continue


if __name__ == '__main__':
    dates = testUtil.get_date("2023-08-12", "2023-08-13")
    print(dates)

    from_city = "HKG"
    to_city = "ICN"

    params["OriginStation"] = from_city
    params["DestinationStation"] = to_city
    positive_or_negative(dates, params)

    # back
    params["OriginStation"], params["DestinationStation"] = params["DestinationStation"], params["OriginStation"]
    positive_or_negative(dates, params)
