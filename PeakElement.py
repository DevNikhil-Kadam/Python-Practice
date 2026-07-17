def peakElement(arr):
        arr.insert(0,float('-inf'))
        arr.append(float('-inf'))
        # Code here
        for i in range(1,len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return True
                
        return False

print(peakElement([1,2,4,5,7,8,9]))