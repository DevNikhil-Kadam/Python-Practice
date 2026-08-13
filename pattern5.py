def pattern1(n):
    for i in range(0,n):
        # for spaces
        for j in range(0,((n-i)-1)):
            print(" ",end="")
        # for characters
        for k in range(0,((2*i)+1)):
            print("*",end="")
        # for spaces
        for l in range(0,(n-i+1)):
            print(" ",end="")
        print()

def pattern2(n):
    for i in range(0,n):
        # for spaces
        for j in range(i):
            print(" ",end="")
        # for stars
        m = 2*(n-i) -1
        for k in range(0,m):
            print("*", end="")
        # for spaces
        for l in range(i):
            print(" ",end="")
        print()

pattern1(6)
pattern2(6)