def binarySubstring(s):
    #code here
    count = 0
    for i in range(len(s)):
        if s[i] == "1":
            count += 1
            
    return (count * (count-1)) // 2

print(binarySubstring("01101"))