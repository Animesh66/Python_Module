from datetime import datetime, timedelta
from time import time

epic_time = time()  # returns the time from origin of OS
print(epic_time)
print("No of Years: ", epic_time/31536000)
dt2 = datetime.now()  # returns the current timestamp
dt3 = datetime.today()
# dt4 = datetime.date(2018, 12, 11)
print("dt2 is: ", dt2)
print("dt3 is: ", dt3)
# print("dt4 is: ", dt4)
print(dt2.strftime("%Y/%m/%d"))  # strftime method  converts date to string format
dt1 = datetime.strptime("2018-12-31", "%Y-%m-%d") + timedelta(days=1)
print(dt1)  # strptime method converts string to date format
print(datetime(2015, 12, 21, 10, 39, 57))
print(f"{dt2.year}/{dt2.month}")  # Returns the
duration = dt2 - dt1
print(duration)
print("Days: ", duration.days)
print("Seconds: ", duration.seconds)