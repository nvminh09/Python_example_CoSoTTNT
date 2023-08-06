# Viết split từng từ trong 1 câu thành những từ riêng biệt.

chuoi = "Tôi là một sinh viên."
print("Chuỗi ban đầu là : ", chuoi)

# split string
chuoiCon = chuoi.split(" ")

print("Các từ của chuỗi : ")
for tu in chuoiCon:
    print(tu)