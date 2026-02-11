def getK_largest(arr, k):
    arr.sort(reverse=True)   
    return arr[k - 1]

print(getK_largest([2, 3, 4, 2, 1, 5], 2))
