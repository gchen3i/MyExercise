#插入排序
arr = [3,44,38,5,36,27,2,46,4,19,50,20,49,21,33]

for i in range(1,int(len(arr))):
    for j in range(i,0,-1):
        if arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
        else:
            break

print(arr)
