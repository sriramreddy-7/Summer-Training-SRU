nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]
n=len(nums)
d={}
for i in nums:
    for j in i:
        if j not in d:
            d[j]=1
        else:
            d[j]+=1
nums=[]
for k,v in d.items():
    if v==n:
        nums.append(k)
nums.sort()
print(nums)