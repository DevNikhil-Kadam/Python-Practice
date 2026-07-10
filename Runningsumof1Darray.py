nums = [1,2,3,4,5]
sumarray = []
for i in range (0, len(nums)):
    if i == 0:
        sumarray.append(nums[i])
    else:
        sumarray.append(nums[i]+sumarray[i-1])
print(sumarray)