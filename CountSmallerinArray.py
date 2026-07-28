def countOfElements(x, arr):
    # code here
    count= 0 
    for i in range(len(arr)):
        if arr[i] <= x:
            count+= 1
    return count

print(countOfElements(10,[1,2,3,4,5,6,7,8,9,10,11]))