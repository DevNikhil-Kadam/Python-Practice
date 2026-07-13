def prime_number(n):
    if n == 1:
        return False
    else:
        for i in range(2, n//2):
            if n % i == 0:
                return False
            else:
                continue
        return True
    
print(prime_number(13))
