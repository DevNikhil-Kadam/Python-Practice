nums = [1,1,0,1,1,1,0,0,1]
count = 0
max_count = 0
for i in range(len(nums)):
    if nums[i] == 1:
        count+=1
    else:
        count = 0
    max_count = max(count,max_count)
print(max_count)