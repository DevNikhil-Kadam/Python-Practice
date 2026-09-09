arr = [0,1,0,3,12]
arr1 = arr.copy()
i = 0
while i < len(arr):
    if arr[i] == 0:
        arr.remove(arr[i])
    else:
        i+=1

for i in range(len(arr),len(arr1)):
    arr.append(0)

print(arr)