a = [1,2,20002,20002,1999,1999,2,1,20002]

b = {}

for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1

result = []
for key in b:
    result.append([key,b[key]])

print(result)