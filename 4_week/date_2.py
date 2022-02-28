import datetime

today = datetime.datetime.now()
d = datetime.timedelta(days = -1)
yesterday = today + d
d = datetime.timedelta(days = 1)
tomorrow = today + d
print(yesterday)
print(today)
print(tomorrow)