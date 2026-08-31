class Solution:

    def partition(self, arr, low, high):

        pivot = arr[high]
        i = low - 1

        for j in range (low,high):
            if arr[j] <= pivot:
                i+=1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]

        return i+1

    def quickSort(self, arr, low, high):

        if low < high:
            partitionIndex = self.partition(arr,low,high)
            self.quickSort(arr,low,partitionIndex - 1)
            self.quickSort(arr, partitionIndex + 1, high)


arr = [5,2,4,6,10,88,1,1,5,6,7,4]
sol = Solution()
sol.quickSort(arr,0, len(arr) -1)
print(*arr)