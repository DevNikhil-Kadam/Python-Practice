def convert(s):
    new_s = ""
    flag = True
    for char in s:
        if flag:
            new_s = new_s + char.upper()
            flag = False
        elif char == " ":
            new_s = new_s + char
            flag = True
        else:
            new_s = new_s + char
            flag = False

    return new_s
print(convert("i love programming"))