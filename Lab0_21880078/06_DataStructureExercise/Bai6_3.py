# Viết chương trình, đếm số lần lặp lại của từng phần tử trong list.

list = [11, 45, 8, 11, 23, 23, 45, 45, 23, 45, 89]
print("List ban đầu ", list)

count_dict = dict()
for item in list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Số lần lặp lại của các phần tử trong list : ", count_dict)