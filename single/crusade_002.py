top = int(input("please input the maxium number:"))
total = odd = even = 0
i = 0
while i <= top:
    total += i
    if (i % 2) == 0:
        even +=i
    else:
        odd +=i

    i +=1

print("零到{0}的累积加为{1}".format(top,total))
print("零到{0}的奇数累积加为{1}".format(top,odd))
print("零到{0}的偶数累积加为{1}".format(top,even))


