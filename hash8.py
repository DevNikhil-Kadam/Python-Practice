
def maxFrequency(nums,k) -> int:

    nums.sort()
    large = float('-inf')
    for i in range(0,len(nums)):
        if nums[i] >= large:
            large = nums[i]                                     #   1,4,8,13

    
    for j in range(0,k):
        index = nums.index()



    freq = {}
    for m in nums:
        if m in freq:
            freq[m] += 1
        else:
            freq[m] = 1
    print(freq)

    key = max(freq, key=freq.get)
    return key

print(maxFrequency([1,4,4,8,9,10,12,12],3))

