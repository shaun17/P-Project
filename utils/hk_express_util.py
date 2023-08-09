
from selenium.webdriver.common.by import By
from datetime import datetime


# 每个时间表详情
def get_schedules(i, flight_date):
    print("起飞时间：", i.find_element(By
                                      .CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME, "time").text)
    print("起飞时间：", flight_date, " ",
          i.find_element(By.CLASS_NAME, "colDeparture").find_element(By.CLASS_NAME, "airport-city").text)
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