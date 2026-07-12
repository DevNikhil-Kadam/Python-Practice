s="niks"
output = True
for i in range(0,len(s)):
    for j in range(i+1, len(s)):
        if s[i] == s[j]:
            output = False
            break
print(output)
# d = dict(enumerate(s))
# print(d)
