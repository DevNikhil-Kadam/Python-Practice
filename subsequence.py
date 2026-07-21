def isSubSeq(s1, s2):
        # code here
        
        start = 0
        count = 0
        
        for char in s1:
            if start < len(s2):
                for i in range(start, len(s2)):
                    if char == s2[i]:
                        count += 1
                        start = i + 1
                        break
                    else:
                        continue
        if count == len(s1):
            return True
        else:
            return False

print(isSubSeq("AXY","YADXCP"))         