arr = [10,8,30,4,5]
x = 5
index = -1
for i in range(0,len(arr)):
    if arr[i] == x:
        index = i
        break
print(index)