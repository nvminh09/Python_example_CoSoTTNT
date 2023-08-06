# Xuất thông tin dòng thứ i trong tập tin *.txt
pathFile = "C:/Users/Ngoc/Downloads/Python_TriTueNhanTao/InputOutputExercise/test1.txt";

with open(pathFile, "r") as tt:
    # Đọc dữ liệu tất cả tác dòng
    d = tt.readlines()
    # xuất thông tin dòng thứ i
    print(d[4])