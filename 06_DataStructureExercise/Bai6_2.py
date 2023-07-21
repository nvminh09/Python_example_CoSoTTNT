# Viết chương trình, xóa phần tử tại vị trí thứ 4 của 1 list, rồi thêm phần tử đó vào :
# - Vị trí thứ 2 của list ban đầu.
# - Vị trí cuối của list ban đầu.

list0 = [3, 5, 6, 8, 1, 13, 9]

print("list ban đầu ", list0)
pt4 = list0.pop(4)
print("Phần tử tại vị trí thứ 4 : ", pt4)
print("list ban đầu sau khi xóa phần tử tại vị trí thứ 4 : ", list0)

list0.insert(2, pt4)
print("list sau khi thêm phần tử vào vị trí thứ 2 : ", list0)

list0.append(pt4)
print("list sau khi thêm phần tử vào vị trí cuối : ", list0)