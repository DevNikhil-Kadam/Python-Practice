arr = [1,1,2,2,2,3,3]
arr2 = []

for i in range(1,len(arr)):
    if arr[i] == arr[i-1]:
        continue
    else:
        arr2.append(arr[i-1])
arr2.append(arr[len(arr)-1])
print(arr2)