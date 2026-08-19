def printReverse(i,n):
    if i > n:
        return
    print(n,end=" ")
    printReverse(i,n-1)

n = int(input("enter a number "))
printReverse(1,n)