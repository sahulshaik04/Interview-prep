def reverse_vowels(s):
    vowels ='aeiouAEIOU'
    left=0
    right=len(s) - 1
    lst=list(s)
    while left<right:
        while left<right and lst[left] not in vowels:
            left+=1
        while left<right and lst[right] not in vowels:
            right-=1
        lst[left],lst[right]=lst[right],lst[left]
        left += 1
        right -= 1
    return ''.join(lst)
s = "hello"
print(reverse_vowels(s))