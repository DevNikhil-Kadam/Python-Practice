def recursiveSum(i,sum):
    if i < 1:
        print(sum)
        return
    recursiveSum(i-1,sum+i)





n = int(input("enter a number "))
recursiveSum(n,0)