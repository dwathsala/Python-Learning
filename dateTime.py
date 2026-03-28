
import datetime
Today = datetime.datetime.now()
print("Today's date and time:", Today)

print(Today.year)
print(Today.month)
print(Today.day)
print(Today.hour)
print(Today.minute)
print(Today.second)
print(Today.microsecond)

datetime1 = datetime.datetime(2027, 12, 25, 10, 30, 45)
print("Custom date and time:", datetime1)

print(datetime1 - Today)

time2 = datetime.time(14, 30, 45)
date2 = datetime.date(2026, 3, 28)
datetime2 = datetime.datetime.combine(date2, time2)
print("Combined date and time:", datetime2)

timedelta1 = datetime.timedelta(days=5, hours=3, minutes=30)
new_datetime = Today + timedelta1
print("New date and time after adding timedelta:", new_datetime)


