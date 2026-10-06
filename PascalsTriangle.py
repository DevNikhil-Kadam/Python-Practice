# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

r = 5
res = []
for i in range(1,r+1):
    n = []
    for j in range(1,i+1):
        if j == 1 or j == i:
            n.append(1)
        else:
            n.append(i-1)
    res.append(n)

print(res)