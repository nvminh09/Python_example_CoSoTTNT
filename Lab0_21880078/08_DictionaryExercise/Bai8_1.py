# Viết chương trình gộp 2 từ điển lại với nhau

dict1 = {'A': 1, 'B': 2, 'C': 3, 'D' : 4}
dict2 = {'E': 55, 'F': 66, 'G': 77}

kq = {**dict1, **dict2}
print(kq)