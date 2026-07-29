def getSecondLargest(arr):
    # code here
    large = float('-inf')
    slarge = float('-inf')
    for i in range(0,len(arr)):
        if arr[i] > large:
            slarge = large
            large = arr[i]
        elif arr[i] > slarge and arr[i] != large:
            slarge = arr[i]
    
    if slarge > float('-inf'):
        return slarge
    else:
        return -1

print(getSecondLargest([1,2,3,4,5,6,7,8,9]))