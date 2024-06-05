# nums = [1,2,3,2]
"""nums = [1,1,1,1,1]
c=0
for i in range(len(nums)):
    if nums.count(i)==1:
        c+=nums[i]
print(c)"""
# nums = [1,1,1,1,1]
nums = [1,2,3,2]
d={}
for n in nums:
    if n in d:
        d[n]+=1
    else:
        d[n]=1
c=0
for keys in d:
    if d[keys]==1:
        c=c+keys
        print(d[keys])
print(c)




