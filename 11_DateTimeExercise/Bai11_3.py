from datetime import datetime

chuoiNgay = "Jun 25 2023  4:20 PM"
datetime_object = datetime.strptime(chuoiNgay, '%b %d %Y %I:%M %p')
print(datetime_object)