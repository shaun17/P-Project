import datetime
import time

time1 = datetime.datetime.strptime('2022-05-09', '%Y-%m-%d')
print(time1.strftime('%d/%m/%Y'))
print(type(time1))
three_days_later = time1 + datetime.timedelta(days=3)

print(three_days_later)
time2 = datetime.datetime.strptime('14/08/2023', '%d/%m/%Y')
print(time2)
print(time2.__str__())
print(type(time2))
print(type(time2.__str__()))


