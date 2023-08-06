# Viết chương trình in ra các số có dạng như sau :
#   5 4 3 2 1 
#   4 3 2 1 
#   3 2 1 
#   2 1 
#   1

n = 8
k = 8
for i in range(0, n + 1):
    for j in range(k - i, 0,-1):
        print( j, end = ' ')
    print()