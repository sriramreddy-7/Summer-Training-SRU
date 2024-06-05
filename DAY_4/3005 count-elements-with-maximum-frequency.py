# nums = [1,2,3,4,5]
# c=0
# for i in range(len(nums)):
#     cc=0
#     cc=nums.count(nums[i])
#     print("cc",cc)
#     if cc>c:
#         c=cc
#     if cc==c:
#         c=c+cc
#     else:
#         continue
# print(c)
nums = [1,2,3,5]
me=max(nums)
me+=1
ht=[0]*me
print(ht)
for i in nums:
    ht[i]=nums.count(i)
    # print(ht)
print(ht)
