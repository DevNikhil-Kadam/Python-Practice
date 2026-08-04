def findDuplicates(arr):
    # code here
    arr = sorted(arr)
    lst = []

    i = 0
    while i < len(arr)-1:

        if arr[i] == arr[i+1]:
            lst.append(arr[i])

        i += 1

    return lst

print(findDuplicates([2,3,1,2,3]))