nums = [3,2,3]

def majorityElement(nums):
    dicts = dict()
    for i in range(0,len(nums)):
        if nums[i] in dicts:
            dicts[nums[i]] +=1
        else:
            dicts[nums[i]] = 1
    maxkey = max(dicts,key=dicts.get)
    print(maxkey)

majorityElement(nums)

