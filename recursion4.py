def printReverse(i,n):
    if i < 1:
        return
    printReverse(i-1,n)
    print(i,end=" ")

n = int(input("enter a number "))
printReverse(n,n)