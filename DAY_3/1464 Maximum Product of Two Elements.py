nums = [1,5,4,5]
mp=0
for i in range(len(nums)):
    cp=0
    for j in range(i+1,len(nums)):
        cp=abs(nums[i]-1) * abs(nums[j]-1)
        if cp>mp:
            mp=cp
print(mp)

