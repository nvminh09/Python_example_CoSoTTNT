# Chương trình tạo ra 1 list từ list1 và list2 (các phần tử là số nguyên).
# Những phần tử của list bao gồm số lẻ của list1 và số chẵn của list2.
def gop_list(list1, list2):
    new_list = []
    
    # Tìm phần tử lẻ của list1 và add vào new_list
    for num in list1:
        if num % 2 != 0:
            new_list.append(num)
    
    # Tìm phần tử chẵn của list2 và add vào new_list
    for num in list2:
        if num % 2 == 0:
            new_list.append(num)
    return new_list

list1 = [1, 2, 3, 8, 4]
list2 = [1, 3, 4, 7, 8, 9]
print("List được tạo thành từ list1 và list2 là : \n", gop_list(list1, list2))