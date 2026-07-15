def findMin(nums):
        pass
        smallest = float('inf')
        for i in range (0, len(nums)):
            if nums[i] <= smallest:
                smallest = nums[i]

        return smallest

print(findMin([1,2,3,4,3,2,1,0,-3,-9]))