# arr = [8,9,3,4,10,32,12]

def insertionsort(arr):

    for i in range(0,len(arr)):
        j = i
        while ( j > 0 and arr[j-1] > arr[j]):
            temp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = temp
            j-=1

arr = [8,9,3,4,10,32,12]
insertionsort(arr)

print(arr)