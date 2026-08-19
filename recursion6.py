def sums(n):
    if n == 0:
        return 0
    return n + sums(n-1)

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
print(sums(3))
print(factorial(4))