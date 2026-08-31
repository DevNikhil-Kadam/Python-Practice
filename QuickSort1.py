class Solution:

    def quickSort(self, arr, low, high):

        if low < high:

            pivotindex = self.partition(arr, low, high)
            self.quickSort(arr,low,pivotindex-1)
            self.quickSort(arr,pivotindex+1,high)

    def partition(self, arr, low, high):

        pivot = arr[high]
        i = low - 1

        for j in range(low,high):
            if arr[j] <= pivot:
                i+=1

                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i+1


arr = [10,7,8,9,15]
sol = Solution()
sol.quickSort(arr,0,len(arr)-1)
print(*arr)