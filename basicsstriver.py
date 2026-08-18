def counts(n):
    count = 0
    while n!= 0:
        if n %20 != 0:
            count+=1
            n = n//10
    return count
def reverse(n):
    op = 0
    while(n>0):
        d = n % 10
        op = (op * 10) + d
        n = n // 10
    return op

print(reverse(1230))

