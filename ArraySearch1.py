def search( arr, x):
        # code here
        for i in range(0, len(arr)):
            if arr[i] == x:
                return i
            
        return -1

print(search([1,2,3,4,5],3))