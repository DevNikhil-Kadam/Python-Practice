n = int(input())
sum = 0
if n == 0:
    print(sum)
elif n < 0:
    print(sum)
else:
    for i in range(1, n+1):
        sum += i
    print(sum)
