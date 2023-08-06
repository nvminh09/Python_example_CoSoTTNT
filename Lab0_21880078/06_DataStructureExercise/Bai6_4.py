# Viết chương trình, đếm số lần lặp lại của từng phần tử trong list.

list1 = [2, 3, 4, 5, 6, 7, 8]
print("List thứ nhất : ", list1)

list2 = [2, 1, 11, 15, 236, 19, 164]
print("List thứ hai : ", list2)

result = zip(list1, list2)
result_set = set(result)
print(result_set)