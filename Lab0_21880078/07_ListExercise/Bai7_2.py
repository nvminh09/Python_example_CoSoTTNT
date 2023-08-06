# Thay 1 giá trị bất kỳ của list bằng 1 giá trị mới

list = [5, 100, 105, 20, 25, 50, 20]

index = list.index(20) # Xác định index của giá trị cần thay.

list[index] = 200 # Thay giá trị mới.
print(list)