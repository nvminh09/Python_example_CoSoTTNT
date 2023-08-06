# Viết chương trình đếm só lượng chữ số của 1 số tự nhiên bất kỳ

num = 75869
count = 0
while num != 0:
    num = num // 10
    count = count + 1
print("Số lượng chữ số : ", count)