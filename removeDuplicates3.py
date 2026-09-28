class Solution:

    def removeDuplicates(self,nums):
        i = 0
        j = i+1
        k = 1
        while j <= (len(nums) - 1):
            if nums[i] == nums[j]:
                j+=1
            else:
                k+=1
                i+=1
                nums[i] = nums[j]
                j+=1
        return k

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))
print(nums)