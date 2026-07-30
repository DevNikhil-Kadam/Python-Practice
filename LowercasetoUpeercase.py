def to_upper(str):
    # code here
    op = ""
    for i in str:
        l = ord(i)
        chars = chr(l-32)
        op+= chars
    return op

print(to_upper("nikhilkadam"))