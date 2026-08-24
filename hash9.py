nums = [15,1,4,4,8,9,10,12,12]

freq = {}

for i in nums:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

mxkey = max(freq, key=freq.get)
print(mxkey)

mnkey = min(freq, key=freq.get)
print(mnkey)