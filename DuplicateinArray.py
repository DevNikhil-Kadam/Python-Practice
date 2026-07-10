nums = [3,1,3,4,2]
dup = 0
for i in range(0,len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] == nums [j]:
            dup = nums[i]
            break
print(dup)