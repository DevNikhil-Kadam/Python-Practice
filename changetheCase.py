s = 'AbCD'
res = ""
for char in s:
    if ord(char) >= 65 and ord(char) <= 90:
        res = s.upper()
    else:
        res = s.lower()
    break
print(res)