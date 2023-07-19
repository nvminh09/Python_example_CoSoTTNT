# Viết chương trình gỡ bỏ nhứng chuỗi rỗng ra khỏi danh sách chuỗi.

str_list = ["Nguyen", "Minh", "", "Văn", None, "Viet", ""]
res_list = []
for s in str_list:
    # Kiểm tra chuỗi rỗng, nếu chuỗi không rỗng thì cho vào res_list.
    if s:
        res_list.append(s)
print(res_list)