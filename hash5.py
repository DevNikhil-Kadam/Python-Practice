# input string
s = input("enter a string")

# declaring hashaary
hash_arr = [0]*256

# precompute
for i in range(len(s)):
    hash_arr[ord(s[i])]+=1

# ask for input
a = int(input("enter number of eklements you want to search : "))
for i in range(a):
    b = input("enter the char:- ")
    occurence = hash_arr[ord(b)]
    print(f"{b} char occured {occurence} times in a given string")