# Viết chương trình gán giá trị phần tử của từ điển thứ nhất cho từ điển thứ hai

defaults = {"designation": 'Developer', "salary": 8000}
employees = ['Minh', 'Tuan']

res = dict.fromkeys(employees, defaults)
print(res)

print(res["Minh"])
