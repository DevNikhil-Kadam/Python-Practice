def getMinMax(arr):
        # code here
        min = float('inf')
        max = float('-inf')
        for i in range(0,len(arr)):
            if arr[i] < min:
                min = arr[i]
            if arr[i] > max:
                max = arr[i]
        return min, max

print(getMinMax([1,4,3,5,4,8,6]))