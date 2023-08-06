# Gộp 2 tập hợp, chỉ giữ lại các phần tử trùng nhau

set1 = {1, 2, 333, 444, 555}
set2 = {333, 444, 555, 6, 7}

set1.intersection_update(set2)
print(set1)