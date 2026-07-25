def getAlternates(arr):
        # Code Here
        l = [arr[0]]
        for i in range(1,len(arr)):
            if i % 2 ==0:
                l.append(arr[i])
                
        return l

print(getAlternates([1,2,3,4,5,6,7,8,9,10,11]))