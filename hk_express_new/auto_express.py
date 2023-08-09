import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.hk_express_util import get_schedules, date_formate_conv
import logging


def get_url(pa):
    return ("https://booking.hkexpress.com/zh-cn/select/?SearchType=" +
            pa.get("SearchType") + "&OriginStation=" +
            pa.get("OriginStation") + "&DestinationStation=" +
            pa.get("DestinationStation") + "&DepartureDate=" +
            pa.get("DepartureDate") + "&Adults=1&rediscoverbooking=false&")


params = {"SearchType": "ONEWAY",
          "OriginStation": "HKG",
          "DestinationStation": "ICN",
          "DepartureDate": "10/8/2023"}


def script_new(url, times):
    browser = webdriver.Chrome()
    browser.get(url)  # 访问网页

    # 延迟wait_times 秒
    wait = WebDriverWait(browser, times)
    # 定位到flightselect_header 标签，也就是航班时刻表
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'flightselect_header')))

    # 先获取时间区间，用于下面遍历每天的航班信息
    schedule = browser.find_element(By.CLASS_NAME, 'dayselector').find_elements(By.TAG_NAME, "li")

    for i in range(len(schedule)):
        flight_date = schedule[i].find_element(By.CLASS_NAME, "date").text
        print(" ————————————")
        print("|", flight_date, "|")
        print(" ————————————")

        if schedule[i].find_element(By.CLASS_NAME, "price").text == "已客满":
            continue
        schedule[i].click()
        # 睡眠5秒
        time.sleep(5)
        # 获取最新dom节点
        schedule = browser.find_element(By.CLASS_NAME, 'dayselector').find_elements(By.TAG_NAME, "li")

        flights = browser.find_elements(By.CLASS_NAME, 'rowFlight')
        for f in flights:
            # each_schedule = f.find_element(By.CLASS_NAME, "custom-adjust-label-position")
            get_schedules(f, flight_date)
            print("")
        print("----------------------------------------------------------------------")


def positive_or_negative(new_date, new_params, wait_time):
    datestr = date_formate_conv(new_date)
    new_params["DepartureDate"] = datestr
    url = get_url(new_params)
    print(url)
    # 超时放大等待响应时间，再舱室两次
    try:
        script_new(url, wait_time)
    except Exception as e:
        while wait_time <= 30:
            logging.error(e)
            wait_time = wait_time + 5
            script_new(url, wait_time)


if __name__ == '__main__':
    from_city = "HKG"
    to_city = "ICN"
    # 获取-3天和+3天的数据
    date = "2023-08-17"
    params["OriginStation"] = from_city
    params["DestinationStation"] = to_city
    positive_or_negative(date, params, 20)

    # back
    params["OriginStation"], params["DestinationStation"] = params["DestinationStation"], params["OriginStation"]
    positive_or_negative(date, params, 20)
