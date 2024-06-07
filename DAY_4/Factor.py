# arr =[3,5,-2,-3,-6,-6]
# s=set(arr)
# print(s)
# print(len(s),len(arr))
# nums = [1,2]
# d={}
# for i in nums:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
# nums = [1,2]
# nums = [2,1,3]
#
# ht=[0]*(max(nums)+1)
# for i in nums:
#     ht[i]=nums.count(i)
# print(ht)
# r=[]
# c=0
# for j in range(len(ht)):
#     if c<=3:
#         if ht[j]>=1:
#             r.append(j)
#             c+=1
#             print("j,c: ",j,c)
#     if c==3:
#         print("c==2",r[1])
#         break
# else:
#     print(-1)
# print(r)
# letters = ["c","f","j"]
# target = "a"
# r = []
# for i in letters:
#     if ord(i) > ord(target):
#         r.append(i)
# me = r[0]
# for j in r:
#     if ord(j) < ord(me):
#         me = j
# print(me)
# arr = [1, 0, 2, 3, 0, 4, 5, 0]
# # for i in range(len(arr)-1):
# i=0
# while i==len(arr)-1:
#     if arr[i]==0:
#         arr.insert(i+1,0)
#         print(arr)
#         if i==len(arr)-1:
#             pass
#         elif i==len(arr)-2:
#             continue
#     else:
#         i=i+1
# print(arr)
# nums = [0,1,2,2,4,4,1]
# d={}
# for i in nums:
#     if i%2==0:
#         if i not in d:
#             d[i]=1
#         else:
#             d[i]+=1
#
# print(d)
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3
# nums2 = [2, 5, 6]
# n = 3
# nums1 = [1]
# m = 1
# nums2 = []
# n = 0
# nums1=nums1+nums2
# print(nums1)
# for i in nums1:
#     if i==0:
#         nums1.remove(i)
#         print(nums1)
# if nums1:
#     nums1.sort()
#     nums1.remove(0)
#     print(nums1)

nums = [1,2,0,0]
k = 34
s=""
for i in nums:
    s=s+str(i)
s=int(s)
nums=[]
for i in str(s+k):
    nums.append(int(i))
print(nums)