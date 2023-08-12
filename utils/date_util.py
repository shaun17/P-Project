from datetime import datetime


def date_formate_conv_whithout_0(time_str):
    # 将字符串解析成datetime对象 5/9/2023
    dt = datetime.strptime(time_str, '%Y-%m-%d')
    # 进行格式化
    return dt.strftime('%-d/%-m/%Y')


def date_formate_conv(time_str):
    # 将字符串解析成datetime对象 5/9/2023
    dt = datetime.strptime(time_str, '%Y-%m-%d')
    # 进行格式化
    return dt.strftime('%d/%m/%Y')

print(date_formate_conv('2022-05-09'))
print(date_formate_conv_whithout_0('2022-05-09'))