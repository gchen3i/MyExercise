#希尔排序（Shell Sort）
arr = [3,44,38,5,36,27,2,46,4,19,50,20,49,21,33]

def InsertSort(array,step):
    for i in range(1, int(len(arr))):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
            else:
                break
    return array

'''
i = 1
length= int(len(arr))
gap = []
while int(len(arr))//(2**i) > 1:
    gap.append(length//(2**i))
    i += 1
gap.append(1)

for step in gap:
    for j in (0,step-1):
        for k in (j,length,step)

'''
