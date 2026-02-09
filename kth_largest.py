def getK_largest(arr,k):
    n = len(arr)
    arr.sort()
    for i in range(n - k, -1, -1):
        if arr[i] != arr[n - 1]:
            return arr[i]
    return -1
print(getK_largest([2,3,4,2,1,5]),2)