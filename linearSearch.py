def linearsearch(nums, target):
    for i in range(0, len(nums)):
            if nums[i] == target:
                return i
    return -1

print(linearsearch([4,6,3,2,1,7,8,9,],6))