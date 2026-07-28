def valEqualToPos(arr):
    # code here
    op = []
    for i in range(len(arr)):
        if i+1 == arr[i]:
            op.append(arr[i])
            
    return op

print(valEqualToPos([15,2,23,4,5,88]))

