def array_check(nums):
    for i in range (len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

print(array_check([1,2,4,5,1]))