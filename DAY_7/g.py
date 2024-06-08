# n=[3,9,4,1,5,7]
# def r(n):
#     c,d=0,0
#     if n[0]>n[1]:
#         c+=n[0]
#         print(n[0])
#         r(n[2:])
#     else:
#         d+=n[1]
#         print(n[1])
#         r(n[3:])
# print(r(n))
# l=[]
# es=0
# os=0
# for i in range(len(n)):
#     if i%2==0:
#         es=es+n[i]
#     else:
#         os=os+n[i]
# l.append(es)
# l.append(os)
# r=[]
# for i in range(len(n)-1):
#     if n[i]>n[i+1]:
#         r.append(n[i])
# print(r)
# print(l)
nums = [1,2,3,4,5]
# m=max(nums)
# m=m+1
# ht=[0]*m
# print(ht)
# for i in nums:
#     ht[i]=nums.count(i)
# print(ht)
# mx=max(ht)
# c=ht.count(mx)
# print(c*mx)
# d={}
# for i in nums:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)
# print(d.get(1))
"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""
# d={
#     'I':1,
#     "V":5,
#     "X":10,
#     "L":50,
#     "C":100,
#     "D":500,
#     "M":1000
# }
# words = ["pay","attention","practice","attend"]
# pref = "at"
# c=0
# for i in range(len(words)):
#     if words[0][1]:
#         if
# nums = [1,100]
# avg=[]
# while nums!=[]:
#     a=min(nums)
#     b=max(nums)
#     avg.append((a+b)/2)
#     nums.remove(a)
#     nums.remove(b)
# print(avg)
nums = [3,2,3]
d={}
for i in nums:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for k,v in d.items():
    if v>len(nums)/2:
        print(k)
        break
