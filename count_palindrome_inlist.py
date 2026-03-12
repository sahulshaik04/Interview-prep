lst=["a","b","c","a","b","a","b","c","a","a","b","c","a","b","c","c","a","a","d","s","s","s","k","b","h","d","a","s"]
def count_palindrome(lst):
    n=len(lst)
    count=0
    left=0
    right=left+2
    while(right<n):
        if lst[left]==lst[right]:
            count+=1
        left+=1
        right+=1
    return count
print(count_palindrome(lst))