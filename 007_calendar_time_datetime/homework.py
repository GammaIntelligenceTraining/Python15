"""
Под каждым комментарием нужно написать одну функцию/программу
Задание в комментарии
input - параметр который функция получает
output - параметр который функция возвращает
"""


# Write a program that converts given string to datetime object
# import datetime
from datetime import datetime, timedelta

sample1 = 'Jan 1 2014 2:43PM'
print(datetime.strptime(sample1, '%b %d %Y %I:%M%p'))
sample2 = '14:20 10/12/22'  # YY/MM/DD
print(datetime.strptime(sample2, '%H:%M %y/%m/%d'))
sample3 = 'Tuesday, September 24, 2019'
print(datetime.strptime(sample3, '%A, %B %d, %Y'))
sample4 = '01.01.1970 - 00:00:01'
print(datetime.strptime(sample4, '%d.%m.%Y - %H:%M:%S'))



# Write a program to print yesterdays, today and tomorrow dates
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print(yesterday)
print(today)
print(tomorrow)

# Write a program to convert given timestamp to dd.mm.yyyy format
some_day = 1014163200
print(datetime.fromtimestamp(some_day).strftime('%d.%m.%Y'))


# Write a function to subtract 2 weeks from timestamp and return new timestamp
# input: timestamp (float)
# output: timestamp (float)

def two_weeks_before(ts):
    d = datetime.fromtimestamp(ts)
    d = d - timedelta(days=14)
    d = d.timestamp()
    return d


print(two_weeks_before(1014163200))
print(datetime.fromtimestamp(1012953600))
