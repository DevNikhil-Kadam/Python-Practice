def occurences(nums, val):
    count = 0
    for i in range(0, len(nums)):
        if nums[i] == val:
            count += 1

    return count

print(occurences([1,2,3,3,4,5,3],4))

