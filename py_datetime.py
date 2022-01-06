from datetime import datetime
from time import time

epic_time = time()  # returns the time from origin
print(epic_time)
dt = datetime.now()  # returns the current timestamp
print(dt)
print(dt.strftime("%Y/%m/%d"))  # strftime conversts date to string format
print(datetime.strptime("2018-12-01", "%Y-%m-%d"))  # strptime converts string to date format
