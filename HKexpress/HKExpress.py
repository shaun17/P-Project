from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import testUtil
import logging


# 每个时间表详情
def get_schedules(i):
    print("起飞时间：", i.find_element(By.CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME, "time").text)
    print("起飞时间：",
          i.find_element(By.CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME, "airport-city").text)
    print("起飞地点编码：",
          i.find_element(By.CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME, "airport-code").text)

    print("飞行时间：", i.find_element(By.CLASS_NAME, "colDuration").find_element(By.CLASS_NAME, "time").text)

    print("到达地点：", i.find_element(By.CLASS_NAME, "colReturn").find_element(By.CLASS_NAME, "time").text)
    print("到达地点：", i.find_element(By.CLASS_NAME, "colReturn").find_element(By.CLASS_NAME, "airport-city").text)
    print("到达地点编码：",
          i.find_element(By.CLASS_NAME, "colReturn").find_element(By.CLASS_NAME, "airport-code").text)

    print("金额：", i.find_element(By.CLASS_NAME, "colPrices").find_element(
        By.CLASS_NAME, "price").text)
    print("单位：", i.find_element(By.CLASS_NAME, "colPrices").find_element(
        By.CLASS_NAME, "currency").text)


def get_url(pa):
    return ("https://booking.hkexpress.com/zh-cn/select/?SearchType=" +
            pa.get("SearchType") + "&OriginStation=" +
            pa.get("OriginStation") + "&DestinationStation=" +
            pa.get("DestinationStation") + "&DepartureDate=" +
            pa.get("DepartureDate") + "&Adults=1&rediscoverbooking=false&")


def script(original_url, wait_times):
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
        get_schedules(f)
        print("----------------------------------------------------------------------")


params = {"SearchType": "ONEWAY",
          "OriginStation": "HKG",
          "DestinationStation": "ICN",
          "DepartureDate": "5/9/2023"}


def date_formate_conv(time_str):
    # 将字符串解析成datetime对象 5/9/2023
    dt = datetime.strptime(time_str, '%Y-%m-%d')
    # 进行格式化
    return dt.strftime('%-d/%-m/%Y')


def positive_or_negative(new_date, new_params):
    for x in new_date:
        times = 20
        datestr = date_formate_conv(x)
        new_params["DepartureDate"] = datestr
        url = get_url(new_params)
        print(url)
        # 超时放大等待响应时间，再舱室两次
        try:
            script(url, times)
        except Exception as e:
            while times <= 30:
                logging.error(e)
                times = times + 5
                script(url, times)
            continue


if __name__ == '__main__':
    dates = testUtil.get_date("2023-09-01", "2023-09-02")
    print(dates)

    from_city = "HKG"
    to_city = "ICN"

    params["OriginStation"] = from_city
    params["DestinationStation"] = to_city
    positive_or_negative(dates, params)

    # back
    params["OriginStation"], params["DestinationStation"] = params["DestinationStation"], params["OriginStation"]
    positive_or_negative(dates, params)
