nums = [1,2,4,5]
miss = 0
for i in range(1,len(nums)):
    if ( nums[i] - nums[i-1] == 2):
        miss = nums[i] - 1
print(miss)