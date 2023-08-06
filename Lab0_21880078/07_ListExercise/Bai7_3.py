# Nhóm các phần tử của 2 list theo chiều ngược nhau.

list1 = [1, 2, 3, 4, 5]
list2 = [11, 22, 33, 44, 55]

for x, y in zip(list1, list2[::-1]):
    print(x, y)