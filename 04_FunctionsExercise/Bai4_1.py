# Viết hàm đệ qui tính tổng các số tự nhiên liên tiếp từ 0 đến m

def Tong(n):
    if n:
        return n + Tong(n - 1)
    else:
        return 0

m = 5
kq = Tong(5)
print(kq)