n = 1004
str_n = str(n)
res = ""
for char in str_n:
    if char == '0':
        res += '5'
    else:
        res += char
print(res)