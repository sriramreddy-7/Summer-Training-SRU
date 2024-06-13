nums = [8,1,2,2,3]
r=[]
for i in range(len(nums)-1):
    c=0
    n = len(nums)
    j=0
    while n>1:
        # print(j,j+1)
        print(nums[j],nums[i])
        if nums[j]<nums[i]:
            c=c+1
        j=j+1
        n=n-1
    r.append(c)
    print(r)
print(r)
# d={}
# for i in range(len(nums)):
#     if


