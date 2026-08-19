def printNums(i,n):
    if i > n:
        return
    print(i,end=" ")
    printNums(i+1,n)

n = int(input("enter a number"))
printNums(1,n)