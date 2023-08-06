# Cho hai tập hợp, tìm phần tử giao của 2 tập

# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 7, 8, 9, 13}
set1 = {111, 2, 3, 4, 5, 333}
set2 = {6, 7, 8, 9, 111, 333}

if set1.isdisjoint(set2):
  print("Hai tập hợp không có phần tử chung.")
else:
  print("Hai tập hợp có phần tử chung là : ")
  print(set1.intersection(set2))