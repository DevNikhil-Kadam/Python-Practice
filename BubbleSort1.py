arr = [13,46,24,52,20,9]

def bubbleSort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(0,i,+1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp

bubbleSort(arr)

print(arr)
 