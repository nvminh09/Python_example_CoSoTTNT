# Viết chương trình kiểm tra tập tin test.txt có rỗng hay không ?

import os

pathFile = "C:/Users/Ngoc/Downloads/Python_TriTueNhanTao/InputOutputExercise/test.txt";

size = os.stat(pathFile).st_size
if size == 0:
    print("test.txt là file rỗng.")
else:
    print("test.txt không phải là file rỗng.")