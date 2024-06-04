nums = [2,5,1,3,4,7]
mid=(len(nums))//2
n1=nums[:mid]
n2=nums[mid:]
nums=[]
for i in range(len(n1)):
    nums.append(n1[i])
    nums.append(n2[i])
print(nums)

