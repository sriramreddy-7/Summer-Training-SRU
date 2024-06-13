nums = [5]
k = 1
r=[]
for i in range(len(nums)):
    result=nums[i:i+k]
    print(result)
    if len(result)==k:
        s=sum(result)
        r.append(s)

print(max(r)/k)
