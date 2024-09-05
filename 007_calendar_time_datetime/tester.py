import datetime

# d = datetime.date(2024, 9, 1)
# today = datetime.date.today()

# print(today.weekday())
# print(today.isoweekday())
#
# if today.isoweekday() in [6, 7]:
#     print('WEEKEND')
# else:
#     print('WORKDAY')

# date1 - date2 = timedelta
# date1 + timedelta = date2
# date2 - timedelta = date1

# diff = today - d
# print(diff)
# print(type(diff))
#
# tdelta = datetime.timedelta(hours=18, minutes=33)
# # print(today + tdelta)
# # print(tdelta.total_seconds())
#
# # t = datetime.time(12, 43, 17)
# # print(t)
# # print(type(t))
#
# dt = datetime.datetime(2024, 9, 4, 18, 30, 15)
# # print((dt - tdelta).time())
# # print(type(dt))
# today = datetime.datetime.today()
# print(today)

# today = datetime.datetime.today()
#
# print(today.strftime('%X'))
#
# date_str = 'Сентябрь 4 2024 Wed, 20:30:15'
# date_str.replace('Сентябрь', 'September')
# dt = datetime.datetime.strptime(date_str, '%B %d %Y %a, %H:%M:%S')
# print(dt)

today = datetime.datetime.today()
print(today.weekday())

# print(today.timestamp())
# ts = 1725471959.043456
# new_datetime = datetime.datetime.fromtimestamp(ts)
# print(new_datetime)

print(datetime.MINYEAR)
print(datetime.MAXYEAR)