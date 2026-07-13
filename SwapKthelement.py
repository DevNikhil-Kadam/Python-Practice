arr = [1,2,3,4,5,6,7,8]
# arr = [5,3,6,1,2,3]
# output = [1,2,6,4,5,3,7,8]
k = 3
print(arr[k-1])
print(arr[-k])
arr[k-1], arr[-k] = arr[-k], arr[k-1]
print(arr)
