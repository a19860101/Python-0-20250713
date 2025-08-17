# import datetime as dt
# t = dt.datetime.today()

from datetime import datetime, timezone, timedelta
# t = datetime.today()

# from datetime import datetime as dt
#
# t = dt.today()
# print(t)
# print(datetime.datetime.today())
# print(datetime.datetime.now())
# print(datetime.datetime.utcnow())

# print(t.date)
# print(t.year)
# print(t.month)
# print(t.day)
# print(t.weekday())
# print(t.isoweekday())
#
# print(t.hour)
# print(t.minute)
# print(t.second)

# 設定時區 timezone
# tz = datetime.timezone(datetime.timedelta(hours=0))
# # print(datetime.datetime.now(tz))

# tz = dt.timezone(dt.timedelta(hours=0))
# print(dt.datetime.now(tz))

# tz = timezone(timedelta(hours=0))
# print(datetime.now(tz))
t = datetime.today()

tomorrow = t + timedelta(days=1)
yesterday = t - timedelta(days=1)
nextweek = t + timedelta(weeks=1)

print(tomorrow)
print(yesterday)
print(nextweek)
