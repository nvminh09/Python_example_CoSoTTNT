# Viết chương trình tính tổng các số tự nhiên liên tiếp từ 1 đến n

s = 0 # Tổng dãy số
n = int(input("Nhập chữ số n : "))
for i in range(1, n + 1, 1):
    s += i
print("Tổng các số tự nhiên từ 1 đến ", n, "là : ", s)