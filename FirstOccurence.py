
def firstOccurence(txt,pat):
    for i in range(len(txt)):
        val = pat[0]
        val2 = txt[i]
        if val2 == val:
            search = txt[i:i+len(pat)]
            if search == pat:
                return i
    return -1
txt = "GeeksForGeeks"
pat = "For"
print(firstOccurence(txt, pat))