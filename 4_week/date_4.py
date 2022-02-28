import datetime

x = datetime.datetime.now()
d = datetime.datetime.strptime('2020-12-31 13:21:52', '%Y-%m-%d %H:%M:%S')
t = datetime.datetime.strptime('2020-12-31 13:21:40', '%Y-%m-%d %H:%M:%S')
total = abs(t - d)
print(int(total.total_seconds()))


