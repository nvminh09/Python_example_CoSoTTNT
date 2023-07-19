# Viết hàm in ra tên, tuổi của một người và gán tên, tuổi mới cho người đó

def TenTuoi(ten, tuoi):
    print("Tên : ", ten, tuoi, "tuổi.")

# In ra tên tuổi ban đầu
print("Tên tuổi cũ là : ")
TenTuoi("Minh ", 26)

# Gán tên tuổi mới
TenTuoiMoi = TenTuoi
# In ra tên tuổi mới
print("\nTên tuổi mới là : ")
TenTuoiMoi("Van Minh", 33)