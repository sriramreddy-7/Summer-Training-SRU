# jewels = "aA"
# stones = "aAAbbbb"
# d={}
# for i in stones:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# # c=0
# # for k,v in d.items():
# #     if jewels in k:
# #         c=c+v
# # print(c)
# print(d)
# c=0
# for i in range(len(jewels)):
#     print(jewels[i])
#     c=c+stones.count(jewels[i])
# print(c)
# s ="abcdefghijklmnopqrstuvwxyzz"
# d={}
# for i in s:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
# x=0
# l=[0]*len(d)
# for k,v in d.items():
#    l[x]=d[k]
#    x=x+1
# print(l)
# for c in range(len(l)-1):
#     print(l[c],l[c+1])
#     if l[c]!=l[c+1]:
#         print(False)
#         break
# else:
#     print(True)

# x =1534236469
#
# imin=-2**31
# imax=2**31-1
# print(imax)
# print(x)


# if x<imin or x>imax:
#     print(0)
# print(imin,imax)
# if x>0:
#     if str(x)[-1]!=0:
#         print(int(str(x)[::-1]))
#     if str(x)[-1]==0:
#         print(int(str(x)[::-2]))
# else:
#     if str(x)[-1]!=0:
#         flag=int(str(x).replace("-","")[::-1])
#         print(-flag)
#     if str(x)[-1]==0:
#         flag = int(str(x).replace("-", "")[::-2])
#         print(-flag)

