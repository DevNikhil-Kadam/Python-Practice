# s = "Geeks"
# output = ""
# for i in range(0,len(s)):
#     if i % 2 == 0:
#         output += s[i]
# print(output)
def isogram(s):
    res = {}
    for char in s:
        if char in res:
            return False
        else:
            res[char] = 1
    return True

print(isogram("nikhil"))
        

