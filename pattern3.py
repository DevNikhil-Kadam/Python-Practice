def pattern(n):
    for i in range(n,0,-1):
        k=1
        for j in range(i):
            print(k,end="")
            k+=1
        print()

pattern(9)