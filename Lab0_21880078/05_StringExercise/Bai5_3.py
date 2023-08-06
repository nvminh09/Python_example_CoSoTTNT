# Viết chương trình xóa ký tự đặc biệt trong một chuỗi

import string

chuoi1 = "/\Minh@ là# một %sinh^ viên. *"
print("Chuỗi ban đầu : \n", chuoi1)

chuoi2 = chuoi1.translate(str.maketrans('', '', string.punctuation))

print("Chuỗi mới là :\n ", chuoi2)