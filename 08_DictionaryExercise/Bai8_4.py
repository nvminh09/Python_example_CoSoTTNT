# Viết chương trình thay thế 1 giá trị trong từ điển.

dict = {
    'emp1': {'Tên': 'A', 'Lương': 75},
    'emp2': {'Tên': 'B', 'Lương': 80},
    'emp3': {'Tên': 'C', 'Lương': 65}
}

dict['emp3']['Tên'] = 'DD'
dict['emp3']['Lương'] = 1000

print(dict)