def checkpalindrome(i,s):
    if (i>=len(s)/2):
        return True
    if s[i] != s[len(s)-i-1]:
        return False
    return checkpalindrome(i+1,s)

print(checkpalindrome(0,"MADAM"))