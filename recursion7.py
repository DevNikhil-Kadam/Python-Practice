def swaparray(l,r):
    if l >= r:
        return
    x = arr[l]
    arr[l] = arr[r]
    arr[r] = x
    swaparray(l+1, r-1)

arr = [1,2,3,4,5]
swaparray(0,len(arr)-1)
print(arr)