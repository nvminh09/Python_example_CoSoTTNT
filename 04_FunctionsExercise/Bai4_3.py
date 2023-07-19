# Viết hàm in ra các giá trị tổng, hiệu của 2 biến nhập vào

def TongHieu(x, y):
    Tong = x + y
    Hieu = x - y
    return print ("Tổng là : ", Tong, "\nHiệu là : ", Hieu)

# get result in tuple format
kq = TongHieu(40, 10)
print(kq)