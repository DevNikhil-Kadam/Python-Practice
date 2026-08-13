def pattern1(n):
    for i in range(0,n):
        for j in range(i+1):
            print("*",end="")
        print()
def pattern2(n):
    for i in range(n-1,0,-1):
        for j in range(i):
            print("*",end="")
        print()
pattern1(5)
pattern2(5)