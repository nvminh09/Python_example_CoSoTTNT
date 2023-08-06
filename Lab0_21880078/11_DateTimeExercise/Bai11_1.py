from datetime import datetime, timedelta

date0 = datetime(2020, 3, 22, 10, 00, 00) # Thời gian bắt đầu
print("Ngày bắt đầu : ")
print(date0)

days = 70 # Số ngày
date1 = date0 + timedelta(days, hours = 12) # Ngày bắt đầu + Số ngày
print("Kết quả : ")
print(date1)