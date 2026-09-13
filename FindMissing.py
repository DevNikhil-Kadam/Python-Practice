nums = [0, 2, 3, 1, 4]
nums.sort()
op = None
for i in range(0,len(nums)-1):
    if nums[i+1] - nums[i] >=2:
        op = nums[i+1] - 1
if op == None:
    print(len(nums))
else:
    print(op)