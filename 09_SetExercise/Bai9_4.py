# Cho 2 tập hợp, tìm những phần tử không trùng nhau của 2 tập hợp.

set1 = {111, 2, 3, 4, 5, 333}
set2 = {6, 7, 8, 9, 111, 333}

set1.symmetric_difference_update(set2)
print(set1)