def concatenatedString(s1,s2):
        #code here
        result = ""
        for char in s1:
            if char not in s2:
                result = result + char
                
        for char in s2:
            if char not in s1:
                result += char
                
        if result == "":
            return -1
        else:
            return result
print(concatenatedString("aacdb","gafd"))