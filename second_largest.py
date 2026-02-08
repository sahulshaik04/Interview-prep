def getSecondLargest(arr):
    n = len(arr)
    arr.sort()
    for i in range(n - 2, -1, -1):
        if arr[i] != arr[n - 1]:
            return arr[i]
    return -1
print(getSecondLargest([2,3,4,2,1,5]))