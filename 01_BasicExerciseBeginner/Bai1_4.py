# Chương trình tính toán tổng số tiền thuế phải nộp trong 3 tháng theo qui định như sau :
# 10,000$ nộp 0%; 10,000$ tiếp theo nộp 10%; 10,000$ tiếp theo nộp 20%.
thuNhap = 90000
thue = 0
print("Thu nhập chịu thuế : ", thuNhap)

if thuNhap <= 10000:
    thue = 0
elif thuNhap <= 20000:
    t = thuNhap - 10000
    thue = t * 10 / 100
else:
    thue = 0
    thue = 10000 * 10 / 100
    thue += (thuNhap - 20000) * 20 / 100

print("Tong so tien thue phai nop la : ", thue)