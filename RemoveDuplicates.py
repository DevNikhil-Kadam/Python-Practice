arr = [1,1,2,2,2,3,3]

def countUnique(arr):
    i = 0
    j = len(arr)-1
    while j<=(len(arr)-1):
        if not arr:
            return 0
        else:
            if arr[i] == arr[j]:
                j+=1
            else:
                i+=1
                arr[i] = arr[j]
            return i+1

print(countUnique(arr))