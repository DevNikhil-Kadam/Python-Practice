nums1 = [10,10,10,10,100,119]
nums2 = [4,10,10,11,119]

def intersectionArray(nums1,nums2):
    i = 0
    j = 0
    result = []

    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            result.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i] < nums2[j]:
            i+=1
        else:
            j+=1
    return result

print(intersectionArray(nums1,nums2))