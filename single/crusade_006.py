#冒泡排序
arr = [3,44,38,5,36,27,2,46,4,19,50,20,49,21,33]
num = len(arr)
for i in range(0,num-1):
    for j in range(0,num-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] =arr[j+1],arr[j]
print(arr)
