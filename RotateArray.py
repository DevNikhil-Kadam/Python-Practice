nums = [1,2,3,4,5,6,7]
k = 20

n = len(nums)
k = k%n

nums.reverse()
print(nums)
nums[:k] = reversed(nums[:k])
nums[k:] = reversed(nums[k:])

print(nums)