# Viết chương trình in ra số hiện tại, số trước đó và tổng của chúng
# (Các số trong khoảng từ 1 đến 11)
print("Chương trình in ra số hiện tại, số trước đó và tổng của chúng : ")
pre_num = 0

for i in range(1, 11):
    sum = pre_num + i
    print("Số hiện tại là ", i, "; số trước đó là ", pre_num, "; Tổng là : ", sum)
    pre_num = i