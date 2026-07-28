def removeVowels(s):
    # code here
    vowels = ['a','e','i','o','u']
    op = ""
    for i in s:
        if i in vowels:
            continue
        else:
            op += i
    return op

print(removeVowels("geekforgeeks"))