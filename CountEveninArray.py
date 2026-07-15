def countEven( nums):
        pass
        count = 0
        for i in range(0, len(nums)):
            if nums[i] %2 == 0:
                count+=1
        return count

print(countEven([1,2,3,4,5,6]))