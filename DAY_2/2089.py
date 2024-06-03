nums=[1,2,5,2,3]
target=2
nums.sort()
r=[]
for i in range(len(nums)):
    if nums[i]==target:
        r.append(i)
print(r)
