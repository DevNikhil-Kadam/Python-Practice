def getMaxOccuringChar(s):
    # code here
    d = {}
    for char in s:
        if char in d:
            d[char] += 1
        else:
            d[char] = 1

    for key,value in d.items():
        if value > 1:
            return key



print(getMaxOccuringChar("abccdeefgh"))