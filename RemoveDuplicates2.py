arr = [1,1,2,2,2,3,3]

# result = [1,2,3,_,_,_,_]
i = 0
j = i + 1
k = 1
while j <= (len(arr) - 1):
    if arr[i] == arr[j]:
        j+=1
    else:
        k+=1
        i+=1
        arr[i] = arr[j]
        j+=1

print(k)
print(arr)
      
