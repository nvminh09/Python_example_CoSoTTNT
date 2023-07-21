# Xóa 1 phần tử có giá trị bất kỳ của 1 list.

list = [5, 20, 15, 20, 25, 50, 20]

def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

kq = remove_value(list, 20)
print(kq)