def isPalindrome(arr):
        # code here
        left = 0
        right = len(arr) - 1
        while(left<right):
            if arr[left] == arr[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

print(isPalindrome([1,2,3,4,3,2,1]))