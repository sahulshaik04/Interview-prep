def move_zeros(nums):
    n=len(nums)
    left=0
    for right in range(n):
        if nums[right]!=0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
    return nums
arr=[0,1,0,2,3,4]
print(move_zeros(arr))      
