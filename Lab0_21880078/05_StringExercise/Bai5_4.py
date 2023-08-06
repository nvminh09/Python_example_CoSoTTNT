# Cho một chuỗi ký tự gồm chữ hoa và chữ thường. VIết chương trình chuyển chuỗi ký tự đã cho
# thành chuỗi mới sao cho chứ thường ở trước, chữ hoa ở sau.

chuoi0 = "MvIaNHn"
print('Chuỗi ký tự ban đầu : ', chuoi0)
chuThuong = []
chuHoa = []
for char in chuoi0:
    if char.islower():
        chuThuong.append(char)
    else:
        chuHoa.append(char)

# Kết nỗi chữ thường va chữ hoa
chuoi1 = ''.join(chuThuong + chuHoa)
print('Result:', chuoi1)