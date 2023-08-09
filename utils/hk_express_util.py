import pandas
from selenium.webdriver.common.by import By
from datetime import datetime


def create_form(excel_file_name):
    form_header = ['出发城市', '出发时间', '航班号', '飞行时间', '到达地点', '到达时间', '金额']
    df = pandas.DataFrame(columns=form_header)
    df.to_excel(excel_file_name, index=False)


def add_info_to_form(excel_file_name, i, flight_date, direction, is_append):
    df = pandas.read_excel(excel_file_name)
    writer = excel_file_name
    if is_append:
        writer = pandas.ExcelWriter(reader=excel_file_name, mode="a", engine="openpyxl")

    row_index = len(df) + 1  # 当前excel内容有几行
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
    df.loc[row_index] = [takeoff_city, takeoff_time, flight_number, flight_time, arrive_city, arrive_time, price]
    df.to_excel(writer, index=False, sheet_name=direction)


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
