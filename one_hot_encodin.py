def one_hot_encoding(arr):
    dic={}
    n=len(arr)
    for i in range(n):
        if arr[i] not in dic:
            dic[arr[i]]=[0]*n
    for i in range(n):
        dic[arr[i]][i]=1
    return dic
arr=['red','blue','red'] 
print(one_hot_encoding(arr))           
