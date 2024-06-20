"""
given two lists , the list data are timings
"""
# h=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
# p=[5,6,5,4,11,2]
# d={}
# n=len(h)
# p1,h1=0,0
# for i in range(n):
#     d[h[i]]=p[i]
#
# print(d,sep="->")
# work={}
# pstart=0
# pend=0
# pmoney=0
#
# for k,v in d.items():
#     start=k[0]
#     end=k[1]
#     money=v
#     print(k[0],k[1],money)
#     if pmoney<=money and start>pend:
#         work[k]=v
#         pstart = k[0]
#         pend = k[1]
#         pmoney = v
#     else:
#         if money>pmoney and pend>start:
#             d.pop((pstart,pend))
#             work[k] = v
#             pstart = k[0]
#             pend = k[1]
#             pmoney = v
#     print(work)
#
# print(work)

nums=[(1,3),(2,5),(4,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
for i in range(1,len(nums)):
    for j in range(0,i):
        if nums[j][1]<=nums[i][0] and b[i]<b[j]+a[i]:
            b[i]=b[j]+a[i]
print(max(b))


