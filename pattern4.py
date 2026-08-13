def pattern(n):
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

pattern(6)