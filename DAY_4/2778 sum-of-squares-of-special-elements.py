nums = [1,2,3,4]
n=len(nums)
p=0
for i in range(0,n):
    if n%(i+1)==0:
        p=p+(nums[i]*nums[i])
        # print(nums[i])
    # print(nums[i])
print(p)
