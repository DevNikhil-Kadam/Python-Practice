def reverse_string( s):
    res = ""
    for i in range(len(s)-1, -1, -1):
        res = res + s[i]
            
    return res
    

print(reverse_string("bengal tiger"))