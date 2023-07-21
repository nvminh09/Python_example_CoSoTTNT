# Xóa 1 phần tử rỗng của 1 list.

list0 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Xóa phần tử rỗng
kq = list(filter(None, list0))
print(kq)
