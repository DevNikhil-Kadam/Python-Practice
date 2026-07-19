def getOddOccurrence(arr):
        # code here 
        out_d = {}
        for i in range(0,len(arr)):
            if arr[i] in out_d:
                out_d[arr[i]] +=1
            else:
                out_d[arr[i]] = 1
        
        for key,value in out_d.items():
            if value %2 != 0:
                return key

print(getOddOccurrence([1,2,3,2,3,1,3]))