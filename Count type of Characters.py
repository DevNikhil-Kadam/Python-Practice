s = "#GeeKs01fOr@gEEks07"
upper = 0
lower = 0
numeric = 0
special = 0
for c in s:
    if (ord(c) >= 65) and (ord(c) <= 90):
        upper += 1
    elif (ord(c) >= 97) and (ord(c) <= 122):
        lower += 1
    elif ( ord(c) >= 48) and (ord(c) <= 57):
        numeric += 1
    else:
        special += 1
print( upper, lower, numeric, special)