def missing_number(nums):
    if nums[0] != 1:
        return 1
    elif nums[len(nums)-1] != int(len(nums)+1): 
        return int(len(nums)+1)
    else:
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 2:
                return (nums[i] - 1)

print(missing_number([1,2,4]))