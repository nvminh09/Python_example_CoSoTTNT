# Viết chương trình in ra các ký tự ở vị trí chỉ số chẵn của một chuỗi.

# Nhập chuỗi ký tự
str = input('Nhập một chuỗi ký tự : ')
print('Ký tự nhập vào là : ', str)

# In ra ký tự ở vị trí chẵn
print('Ký tự ở vị trí chẵn : ')
for i in range (0, len(str), 2):
    print('\nKý tự tại vị trí ', i, 'là : ', str[i])