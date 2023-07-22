# Viết chương trình kiểm tra giá trị có tồn tại trong từ điển hay không.

dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
v = 33
if v in dict.values():
    print('Giá trị', v ,'có tồn tại trong từ điển.')
else:
    print('Giá trị ',v,' không tồn tại trong từ điển.')