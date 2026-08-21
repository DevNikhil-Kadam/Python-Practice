a = int(input("enter a size of array: "))
arr = []
for i in range(a):
    arr.append(int(input(f"enter {i+1}th elemenet of array:- ")))
b = int(input("how many numbers you want to find:- "))

hash_arr = [0]*13
for i in range(0,len(arr)):
    hash_arr[arr[i]] +=1

for i in range(1,b+1):
    c=int(input("enter a number to search:- "))
    def findOccurence(c):
        if c <=12:
            print(f"Th number {c} occured {hash_arr[c]} times in array")
        else:
            print("number not found")
    findOccurence(c)