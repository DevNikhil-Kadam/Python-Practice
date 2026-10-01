class solution:
    def leadersinArray(self,nums):
        n = len(nums)
        if n == 0:
            return []
        max_right = nums[n-1]
        leader = []
        leader.append(max_right)

        for i in range(n-2, -1, -1):
            if nums[i] > max_right:
                leader.append(nums[i])

            max_right = max(max_right, nums[i])
        leader.reverse()
        return leader

nums = [1, 2, 5, 3, 1, 2]
sol = solution()
print(sol.leadersinArray(nums))