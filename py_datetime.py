from datetime import datetime
from time import time

dt = datetime.now()
print(dt)
print(dt.strftime("%Y/%m/%d"))  # strftime conversts date to string format
print(datetime.strptime("2018/12/01","%Y/%m/%d"))
