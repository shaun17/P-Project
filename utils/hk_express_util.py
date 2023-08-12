import numpy as np
import pandas
from openpyxl.utils import get_column_letter
from selenium.webdriver.common.by import By
from datetime import datetime


def get_url(pa):
    return ("https://booking.hkexpress.com/zh-cn/select/?SearchType=" +
            pa.get("SearchType") + "&OriginStation=" +
            pa.get("OriginStation") + "&DestinationStation=" +
            pa.get("DestinationStation") + "&DepartureDate=" +
            pa.get("DepartureDate") + "&Adults=1&rediscoverbooking=false&")


def create_excel_file(excel_file_name):
    df = get_df_from_write()
    df.to_excel(excel_file_name, index=False)


def load_file(file_name):
    return pandas.read_excel(file_name)


def create_write(excel_file_name):
    return pandas.ExcelWriter(excel_file_name, mode="a", engine="openpyxl")


def get_df_from_write():
    form_header = ['出发城市', '出发时间', '航班号', '飞行时间', '到达地点', '到达时间', '金额']
    return pandas.DataFrame(columns=form_header)


def get_info_from_form(i, flight_date, infos):
    takeoff_time = flight_date + " " + i.find_element(By.CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME,
                                                                                                  "time").text
    takeoff_city = i.find_element(By.CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME, "airport-city").text
    flight_number = i.find_element(By.CLASS_NAME, "colDuration").find_element(By.CLASS_NAME,
                                                                              "flight-number_list").text.strip()
    flight_time = i.find_element(By.CLASS_NAME, "colDuration").find_element(By.CLASS_NAME, "time").text.strip().replace(
        "flight duration", "")

    arrive_city = i.find_element(By.CLASS_NAME, "colReturn").find_element(By.CLASS_NAME, "airport-city").text
    arrive_time = i.find_element(By.CLASS_NAME, "colReturn").find_element(By.CLASS_NAME, "time").text
    price = i.find_element(By.CLASS_NAME, "colPrices").find_element(
        By.CLASS_NAME, "price").text
    infos.append([takeoff_city, takeoff_time, flight_number, flight_time, arrive_city, arrive_time, price])


# 每个时间表详情
def get_schedules(i, flight_date):
    print("起飞时间：", flight_date, " ",
          i.find_element(By.CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME, "time").text)
    print("起飞地点：", i.find_element(By.CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME, "airport-city").text)
    print("起飞地点编码：",
          i.find_element(By.CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME, "airport-code").text)

    print("飞行时间：",
          i.find_element(By.CLASS_NAME, "colDuration").find_element(By.CLASS_NAME, "time").text.strip().replace(
              "flight duration", ""))
    print("航班号：",
          i.find_element(By.CLASS_NAME, "colDuration").find_element(By.CLASS_NAME, "flight-number_list").text.strip())

    print("到达时间：", i.find_element(By.CLASS_NAME, "colReturn").find_element(By.CLASS_NAME, "time").text)
    print("到达地点：", i.find_element(By.CLASS_NAME, "colReturn").find_element(By.CLASS_NAME, "airport-city").text)
    print("到达地点编码：",
          i.find_element(By.CLASS_NAME, "colReturn").find_element(By.CLASS_NAME, "airport-code").text)

    print("金额：", i.find_element(By.CLASS_NAME, "colPrices").find_element(
        By.CLASS_NAME, "price").text)
    # print("单位：", i.find_element(By.CLASS_NAME, "colPrices").find_element(
    #     By.CLASS_NAME, "currency").text)


def date_formate_conv(time_str):
    # 将字符串解析成datetime对象 5/9/2023
    dt = datetime.strptime(time_str, '%Y-%m-%d')
    # 进行格式化
    return dt.strftime('%-d/%-m/%Y')


def to_excel_auto_column_weight(df, sheet_name, p_writer):
    #  计算表头的字符宽度
    column_widths = (
        df.columns.to_series().apply(lambda x: len(x.encode('gbk'))).values
    )
    #  计算每列的最大字符宽度
    max_widths = (
        df.astype(str).applymap(lambda x: len(x.encode('gbk'))).agg(max).values
    )
    # 计算整体最大宽度
    widths = np.max([column_widths, max_widths], axis=0)
    # 设置列宽
    worksheet = p_writer.sheets[sheet_name]
    for i, width in enumerate(widths, 1):
        # openpyxl引擎设置字符宽度时会缩水0.5左右个字符，所以干脆+2使左右都空出一个字宽。
        worksheet.column_dimensions[get_column_letter(i)].width = width + 2
