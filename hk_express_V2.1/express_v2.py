import datetime
import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.hk_express_util import create_excel_file, create_write, \
    get_info_from_form, get_df_from_write, load_file, to_excel_auto_column_weight, get_url

params = {"SearchType": "ONEWAY",
          "OriginStation": "HKG",
          "DestinationStation": "ICN",
          "DepartureDate": "10/8/2023"}


def find_all(schedule, sets, start_date, end_date, browser, infos):
    org_date = None
    for i in range(len(schedule)):
        # 查询的时间
        org_date = datetime.datetime.strptime(schedule[i].find_element(By.CLASS_NAME, "date").text, "%d/%m/%Y")

        if org_date not in sets and start_date <= org_date <= end_date:
            sets.add(org_date)

            print(" ————————————")
            print("|", org_date.date(), "|")
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
                get_info_from_form(f, org_date.strftime("%d/%m/%Y"), infos)

    return org_date < end_date


def script_new(browser, dates, url, times, new_sheet, new_writer):
    browser.get(url)  # 访问网页
    start_date = dates[0]
    end_date = dates[-1]
    # 延迟wait_times 秒
    wait = WebDriverWait(browser, times)
    # 定位到flightselect_header 标签，也就是航班时刻表
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'flightselect_header')))

    flag = True  # back tag
    sets = set()  # datetime set
    infos = []
    while flag:

        # 先获取时间区间，用于下面遍历每天的航班信息
        schedule = browser.find_element(By.CLASS_NAME, 'dayselector').find_elements(By.TAG_NAME, "li")
        print(schedule)
        flag = find_all(schedule, sets, start_date, end_date, browser, infos)
        if not flag:
            break
        browser.find_element(By.CSS_SELECTOR, ".next").click()
        time.sleep(5)

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


def positive_or_negative(range_dates, new_params, wait_time, file_name, new_sheet, new_writer):
    datestr = dates[0].strftime("%-d/%-m/%Y")

    new_params["DepartureDate"] = datestr
    url = get_url(new_params)
    print(url)
    # 超时放大等待响应时间，再舱室两次
    browser = webdriver.Chrome()

    try:
        script_new(browser, range_dates, url, wait_time, new_sheet, new_writer)
    except Exception as e:
        while wait_time <= 30:
            logging.error(e)
            wait_time = wait_time + 5
            script_new(browser, range_dates, url, wait_time, new_sheet, new_writer)


if __name__ == '__main__':
    from_city = "HKG"
    to_city = "ICN"
    stay = 2

    dates = [datetime.datetime.strptime("2023-08-17", "%Y-%m-%d"),
             datetime.datetime.strptime("2023-09-01", "%Y-%m-%d")]

    params["OriginStation"] = from_city
    params["DestinationStation"] = to_city

    excel_file_name = 'test.xlsx'
    create_excel_file(excel_file_name)

    positive_or_negative(dates, params, 20, excel_file_name, "GO", None)
    print("----------------------------------------------------------------------")

    # flight return
    # use `write` to load file and create a new sheet
    writer = create_write(excel_file_name)
    params["OriginStation"], params["DestinationStation"] = params["DestinationStation"], params["OriginStation"]

    dates = list(map(lambda x: x + datetime.timedelta(days=2), dates))
    positive_or_negative(dates, params, 20, excel_file_name, "RETURN", writer)

    # reload file, adjust column weight
    df = load_file(excel_file_name)
    for x in ["GO", "RETURN"]:
        to_excel_auto_column_weight(df, x, writer)

    writer.close()
    print("")
    print("###### CONGRATULATION !!! ######")
