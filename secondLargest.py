nums = [1, 1, 2, 2, 3, 3]
large = float('-inf')
slarge = large
for i in range (0, len(nums)):
    if nums[i] > large and nums[i] != slarge:
        slarge = large
        large = nums[i]
    elif nums[i] > slarge and nums[i] != large:
        slarge = nums[i]
print(slarge)