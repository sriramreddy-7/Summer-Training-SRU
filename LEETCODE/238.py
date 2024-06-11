nums = [0]
print(nums)
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]==0 and nums[j]!=0:
            nums[j],nums[i]=nums[i],nums[j]
c=0
while all(nums)==False:
    nums.remove(0)
    c=c+1
for i in range(c):
    nums.append(0)
print(nums)