def removeDuplicates(s):
        pass
        output={}
        for char in s:
            if char in output:
                output[char]+=1
            else:
                output[char] = 1

        str1 = ""
        for key,value in output.items():
                str1 = str1 + key

        return str1

print(removeDuplicates("programmings"))