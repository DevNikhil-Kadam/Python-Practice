nums = [3,1,-2,-5,2,-4]

def rearrangeArray(nums):
    pos = []
    nos = []
    for i in range(0,len(nums)):
        if nums[i] >0:
            pos.append(nums[i])
        else:
            nos.append(nums[i])
    p = 0
    n = 0
    for i in range(0,len(nums)):
        if i == 0 or i % 2 == 0:
            nums[i] = pos[p]
            p+=1
        else:
            nums[i] = nos[n]
            n+=1
    return nums, pos, nos
            
# nums = [3,1,-2,-5,2,-4]
print(rearrangeArray(nums))
