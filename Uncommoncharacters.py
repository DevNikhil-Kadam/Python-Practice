def uncommonChars(s1, s2):
    #code here
    op = ""
    for char in s2:
        if char in s1:
            continue
        else:
            if char not in op:
                op += char
            
    for char in s1:
        if char in s2:
            continue
        else:
            if char not in op:
                op += char
    
    op = ''.join(sorted(op))
    return op

print(uncommonChars("geeksforgeeks","geeksquiz"))