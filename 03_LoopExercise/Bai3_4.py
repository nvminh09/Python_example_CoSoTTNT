# Viết chương trình n giai thừa

P = 1 # Giai thừa
n = int(input("Nhập chữ số n : "))
for i in range(1, n + 1, 1):
    P = P * i
print(n,"! = ", P)