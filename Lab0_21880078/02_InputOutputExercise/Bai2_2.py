# Viết chương trình sử dụng string.format() để định dạng 3 biến

soLuong = 3
tongTien = 1350000
gia = 450000
str = "Tôi có {1} đồng, vì vậy tôi có thể mua {0} trái bóng với giá {2:.2f}/trái."
print(str.format(soLuong, tongTien, gia))