import hashlib
import time
import requests
import datetime
import pandas


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


# 创建一个名字为excel_file_name的excel文件
# 这里把表头设置为（姓名name，年龄age，性别gender，城市city，技能skill）
def create_form(excel_file_name):
    form_header = ['姓名name', '年龄age', '性别gender', '城市city', '技能skill']
    df = pandas.DataFrame(columns=form_header)
    df.to_excel(excel_file_name, index=False)


def create_write(excel_file_name):
    return pandas.ExcelWriter(excel_file_name, mode="a", engine="openpyxl")


# 这里把信息插入到excel里面
def add_info_to_form(excel_file_name, name, age, gender, city, skill):
    df = pandas.read_excel(excel_file_name)
    row_index = len(df) + 1  # 当前excel内容有几行
    df.loc[row_index] = [name, age, gender, city, skill]
    df.to_excel(excel_file_name, index=False)


def add_info_to_sheet(excel_file_name, name, age, gender, city, skill, writer, isnew):
    if isnew:
        df = pandas.DataFrame(columns=['姓名name', '年龄age', '性别gender', '城市city', '技能skill'])
    else:
        print("333")
        df = pandas.read_excel(excel_file_name, sheet_name="2222")
    row_index = len(df) + 1  # 当前excel内容有几行
    df.loc[row_index] = [name, age, gender, city, skill]
    if isnew:
        df.to_excel(writer, index=False, sheet_name="2222")
    else:
        df.to_excel(writer, index=False)
    writer.close()


def add_info_to_sheet_2(info, write):
    df = pandas.DataFrame(columns=['姓名name', '年龄age', '性别gender', '城市city', '技能skill'])
    row_index = len(df) + 1  # 当前excel内容有几行
    for x in info:
        df.loc[row_index] = x
        row_index = row_index + 1
    df.to_excel(write, index=False, sheet_name="22222")


def add_info_to_form_2(name, info):
    df = pandas.read_excel(name)
    row_index = len(df) + 1  # 当前excel内容有几行
    for x in info:
        df.loc[row_index] = x
        row_index = row_index + 1
    df.to_excel(name, index=False)


if __name__ == "__main__":
    file_name = 'test.xlsx'
    create_form(file_name)
    info1 = [['张瑞', 27, '女', '杭州', '吃'], ['张瑞', 27, '女', '杭州', '吃']]
    add_info_to_form_2(file_name, info1)
    # add_info_to_form(file_name, '张瑞', 27, '女', '杭州', '吃')

    writer = create_write(file_name)
    info2 = [['张瑞2', 27, '女2', '杭州2', '吃2'], ['张瑞', 27, '女', '杭州', '吃']]
    add_info_to_sheet_2(info2, writer)
    # add_info_to_sheet(file_name, '张瑞3', 327, '3女', '杭州3', '吃', writer, False)
    writer.close()
