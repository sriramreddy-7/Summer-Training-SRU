nums = [1,2,3,4]
k = 1
count=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)-1):
        if nums[j]==nums[j+1]:
            if (i*j)%k==0:
                count+=1
print(count)

