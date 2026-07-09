nums = [1,2,3,4,5]
output = []

for i in range(0,len(nums)):
    if i == 0:
        output.append(nums[-1])
    else:
        output.append(nums[i-1])
print(output)