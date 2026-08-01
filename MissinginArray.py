def missingNum( arr):
    # code here
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        
    n = len(arr)+1
    exact_sum = (n*(n+1)) // 2
    
    return exact_sum - sum

print(missingNum([1,2,3,4,6,7,8]))