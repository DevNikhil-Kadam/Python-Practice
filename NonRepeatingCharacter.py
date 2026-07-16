def nonRepeatingChar(s):
        #code here
        output = {}
        for char in s:
            if char in output:
                output[char] +=1
            else:
                output[char] = 1
                
        for key,value in output.items():
            if value == 1:
                return key
                
        return '$'
    
print(nonRepeatingChar("geeksforgeeks"))