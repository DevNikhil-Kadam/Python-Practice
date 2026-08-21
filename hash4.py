s = input("Enter a string: ")
print(s)

# Precompute
hash_arr = [0] * 26

for i in range(len(s)):
    hash_arr[ord(s[i]) - ord('a')] += 1

print(hash_arr)

# Queries
b = int(input("Number of elements you want to search: "))

for i in range(b):
    c = input("Enter char: ")

    occurrence = hash_arr[ord(c) - ord('a')]

    print(f"{c} occurred {occurrence} times")