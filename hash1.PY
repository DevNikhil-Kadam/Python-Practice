arr = [1,2,3,2,3]
n = 5
# precompute by hasing
hash = [0] * 13
print(hash) 
for i in range(0,len(arr)):
    hash[arr[i]] +=1

def findOccurence(d):
    print(hash[d])

findOccurence(3)