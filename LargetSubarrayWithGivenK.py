class solution:
    def longestSubArray(self,nums,k):

        n = len(nums)
        maxlen = 0

        left = 0
        right = 0

        sum = nums[0]

        while right < n:

            while left <= right and sum > k:
                sum -= nums[left]
                left +=1

            if sum == k:
                maxlen = max(maxlen,right-left+1)

            right += 1
            if right < n:
                sum += nums[right]

        return maxlen


sol = solution()
nums = [10,5,2,7,1,9]
k = 15
print(sol.longestSubArray(nums,k))
