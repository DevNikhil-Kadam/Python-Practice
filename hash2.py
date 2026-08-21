a = int(input("enter a number of elements in array"))
arr = []
for i in range(0,a):
    arr.append(int(input("enter the element: ")))

    # arr[i] = int(input(f"enter {a}th element "))

n = int(input("how many numbners you want to search ? "))

hash = [0]*13
for i in range(0,len(arr)):
    hash[arr[i]]+=1

for i in range(0,n):
    m = int(input("enter a number to search in array : "))
    
    def findOccurence(m):
        print(f"{m} is occuring {hash[m]} times in array")
    findOccurence(m)

