# names = ["Alice","Bob","Bob"]
# heights = [155,185,150]
# d={}
# for i in range(len(names)):
#     d[heights[i]]=names[i]
# heights.sort(reverse=True)
# l=[]
# print(names)
# print(d)
# for i in heights:
#     for k,v in d.items():
#         if i==k:
#             l.append(v)
# print(l)
# nums = [-1,10,6,7,-7,1]
# d={}
# for i in nums:
#     if -i in nums:
#         d[i]=-i
# print(max(d))
# arr = [0,1,2,3,4,5,6,7,8]
# barr=[]
# for i in arr:
#     barr.append(bin(i)[2:])
# n=[]
# d={}
# def bsum(i,d):
#     rem=0
#     c=0
#     i=int(i)
#     print("i",i)
#     d[i]=0
#     while i>0:
#         rem=i%10
#         print("rem",rem)
#         if rem==1:
#             c=c+1
#             print("c",c)
#         i=i//10
#     print("d i",d[i])
#     d[i]=c
#     print("d i",d[i])
#
#
# for i in barr:
#     bsum(i,d)
#
# print(d)

# nums1 = [1,1,3,2]
# nums2 = [2,3]
# nums3 = [3]
# n=nums1+nums2+nums3
# l=[]
# for i in n:
#     if i in nums1 and i in nums2 or i in nums1 and i in nums3 or i in nums2 and i in nums3:
#         l.append(i)
# print(list(set(l)))
# d={}
# for i in words[0]:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# s=[]
# for k,v in d.items():
#     for i in words:
#         if i==k:
#             print()

words = ["bella","label","roller"]
r=[i for i in words[0]]
l=[]
print(r)
for i in words:
    for j in i:
        if j in r:
            print(j)
s=list(set)
print(l)



