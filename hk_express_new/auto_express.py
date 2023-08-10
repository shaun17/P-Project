import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.hk_express_util import date_formate_conv, create_form, create_write, \
    get_info_from_form, get_df_from_write, load_file, to_excel_auto_column_weight


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


def script_new(url, times, file_name, new_sheet, new_writer):
    browser = webdriver.Chrome()
    browser.get(url)  # 访问网页

    # 延迟wait_times 秒
    wait = WebDriverWait(browser, times)
    # 定位到flightselect_header 标签，也就是航班时刻表
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'flightselect_header')))

    # 先获取时间区间，用于下面遍历每天的航班信息
    schedule = browser.find_element(By.CLASS_NAME, 'dayselector').find_elements(By.TAG_NAME, "li")
    infos = []
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
            get_info_from_form(f, flight_date, infos)

    print(infos)
    if new_writer:
        df = get_df_from_write()
        foreach_everyone(df, infos)
        df.to_excel(new_writer, index=False, sheet_name=new_sheet)
    else:
        df = load_file(excel_file_name)
        foreach_everyone(df, infos)
        df.to_excel(excel_file_name, index=False, sheet_name=new_sheet)


def foreach_everyone(df, infos):
    row_index = len(df) + 1  # 当前excel内容有几行
    for x in range(len(infos)):
        df.loc[row_index] = infos[x]
        row_index = row_index + 1


def positive_or_negative(new_date, new_params, wait_time, file_name, new_sheet, new_writer):
    datestr = date_formate_conv(new_date)
    new_params["DepartureDate"] = datestr
    url = get_url(new_params)
    print(url)
    # 超时放大等待响应时间，再舱室两次
    try:
        script_new(url, wait_time, file_name, new_sheet, new_writer)
    except Exception as e:
        while wait_time <= 30:
            logging.error(e)
            wait_time = wait_time + 5
            script_new(url, wait_time, file_name, new_sheet, new_writer)


if __name__ == '__main__':
    from_city = "HKG"
    to_city = "ICN"
    # 获取-3天和+3天的数据
    date = "2023-08-17"
    params["OriginStation"] = from_city
    params["DestinationStation"] = to_city

    excel_file_name = 'test.xlsx'
    create_form(excel_file_name)

    positive_or_negative(date, params, 20, excel_file_name, "GO", None)
    print("----------------------------------------------------------------------")

    # flight return
    # use `write` to load file and create a new sheet
    writer = create_write(excel_file_name)
    params["OriginStation"], params["DestinationStation"] = params["DestinationStation"], params["OriginStation"]
    positive_or_negative(date, params, 20, excel_file_name, "RETURN", writer)

    # reload file, adjust column weight
    df = load_file(excel_file_name)
    for x in ["GO", "RETURN"]:
        to_excel_auto_column_weight(df, x, writer)

    writer.close()
    print("")
    print("###### CONGRATULATION !!! ######")
