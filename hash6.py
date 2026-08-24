# input
s = input("enter an input string:- ")

# DECLARING HASH AARRAY
hash_arr = [0] * 256

# precompute
for i in range(len(s)):
    hash_arr[ord(s[i])]+=1

# ask for input no
a = int(input("how many characters you want to search"))

# fetch give count and print
while(a!=0):
    b = input("enter a char:- ")
    print(hash_arr[ord(b)])
    a-=1