nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
s1 = set(nums1)
s2 = set(nums2)

s3 = s1.intersection(s2)
s4 = list(s3)
s4.sort()
print(s4)