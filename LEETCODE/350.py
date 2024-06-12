# nums1 = [1,2,2,1]
# nums2 = [2,2]
# d1={}
# d2={}
# for i in nums1:
#     if i not in d1:
#         d1[i]=1
#     else:
#         d1[i]+=1
# print(d1)
# for i in nums2:
#     if i not in d2:
#         d2[i]=1
#     else:
#         d2[i]+=1

# nums = [2,11,10,1,3]
# k = 10
# c=0
# for i in nums:
#     if i<k:
#         c=c+1
# print(c)
nums = [-2,-1,-1,1,2,3]
# i=0
# j=len(nums)-1
# while i<=j:
#     if nums[i]>0:
#         print(len(nums[i:]))
#         break
#     elif nums
p=0
n=0
for i in nums:
    if i<0:
        n=n+1
    else:
        if i>0:
            p=p+1
if p>n:
    print(p)
else:
    print(n)



