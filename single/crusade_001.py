#九九乘法表
#第一种
i = 1
while i <= 9:
    j = 1
    while j <= i:
        plus = i * j
        if j != i :
            print("{0}x{1}={2}".format(i,j,plus),end="\t")
        else:
            print("{0}x{1}={2}".format(i, j, plus), end="\n")
        j += 1
    i +=1

#第二种
for m in range(1,10):
    for n in range(1,m+1):
        print("{0}*{1}={2}".format(m,n,(m*n)),end="\t")
    print()