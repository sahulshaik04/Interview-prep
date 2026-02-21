arr=[1,2,4,5]
n=5
s=n*(n+1)//2
asum=0
for x in arr:
    asum+=x
missing_number=s-asum
print(missing_number)