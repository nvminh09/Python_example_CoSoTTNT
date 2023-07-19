# Cho 2 list ban đầu là list1 và list2. 
# Hãy tạo ra một list mới gồm các phần tử có chỉ số lẻ của list1 và chỉ số chẵn của list2

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
kq = list()

le = list1[1::2]
print("Phần tử có chỉ số lẻ của list1 : ")
print(le)

chan = list2[0::2]
print("Phần tử có chỉ số chẵn của list2 : ")
print(chan)

print("Printing Final third list")
kq.extend(le)
kq.extend(chan)
print(kq)