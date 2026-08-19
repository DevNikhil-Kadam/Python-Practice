def printname(i,n):
    if i > n:
        return
    print("nikhil")
    printname(i+1,n)

n = int(input("enter a numbe"))
printname(1,n)