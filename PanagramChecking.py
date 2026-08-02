def checkPangram(s):
    #code here
    arr = [0] * 26
    s = s.lower()
    for char in s:
        if char.isalpha():
            arr[ord(char) - 97] += 1
            
    for count in arr:
        if count == 0:
            return False
        else:
            continue
    return True

print(checkPangram("Bawds jog, flick quartz, vex nymph"))