def getPairs(arr):
    arr.sort()
    ans = []

    i = 0
    j = len(arr)-1

    while i < j:

        s = arr[i] + arr[j]

        if s == 0:

            ans.append([arr[i], arr[j]])

            left = arr[i]
            right = arr[j]

            while i < j and arr[i] == left:
                i += 1

            while i < j and arr[j] == right:
                j -= 1

        elif s < 0:
            i += 1
        else:
            j -= 1

    return ans

print(getPairs([-4,3,2,1,3,5,6,4,7,-2]))