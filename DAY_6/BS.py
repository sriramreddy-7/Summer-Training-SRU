# nums = [-1,0,3,5,9,12]
# target=15
# i=0
# j=len(nums)-1
# f=0
# while i<=j:
#     mid = (i + j) // 2
#     if nums[mid]==target:
#         f=1
#         print(mid)
#         break
#     elif target<nums[mid]:
#         j=mid-1
#     else:
#         i=mid+1
# if f==0:
#     print(None)
# nums = [-1,1,2,3,1]
# nums.sort()
# target = 2
# c=0
# start=0
# end=len(nums)-1
# while start<=end:
#     if nums[start]+nums[end]<target:
#         c+=end-start
#         start+=1
#     else:
#         end-=1
# print(c)
