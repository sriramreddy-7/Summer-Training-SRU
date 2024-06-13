nums = [2,0,1]
mx=nums[0]
for i in nums:
    if i>mx:
        mx=i
ht=[0]*(mx+1)
for i in nums:
    ht[i]=nums.count(i)
nums=[]
for j in range(len(ht)):
    nums.extend([j]*ht[j])
print(nums)
