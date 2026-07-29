def swapElements(arr):
    #Code here
    end = len(arr) -2
    for i in range(0,end):
        x = arr[i]
        arr[i] = arr[i+2]
        arr[i+2] = x
    return arr

print(swapElements([1,2,3,4,5]))