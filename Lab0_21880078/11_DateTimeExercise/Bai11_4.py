# Tính khoảng thời gian giữa 2 ngày
from datetime import datetime

date1 = datetime(2022, 2, 25).date()
date2 = datetime(2023, 9, 17).date()

delta = None
if date1 > date2:
    print("date1 sau date2.")
    delta = date1 - date2
else:
    print("date2 sau date1")
    delta = date2 - date1
print("Khoảng thời gian : ", delta.days, " ngày.")