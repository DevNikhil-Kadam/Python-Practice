def removeSpaces(s):
    # code here
    op = ""
    for i in s:
        if i == " ":
            continue
        else:
            op += i
    return op

print(removeSpaces("my name is don"))