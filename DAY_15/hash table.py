# c=0
# def fun(hours):
#     i=0
#     j=len(hours)-1
#
# hours = [12,12,30,24,24]
# print(fun(hours))

# words = ["bella","label","roller"]
#
# l=list(map(str,words[0]))
# print(l)
#
#
# c=[]
# for i in l:
#     for i in words:
#         c.append(i)

# s = "cb34"
# for i in range(len())
# arr = [37,12,28,9,100,56,80,5,12]
# arr.sort()
# print(arr)
# t = []
# i=0
# d={}
# while i<len(arr) - 1:
#     if arr[i]!=arr[i+1]:
#         d[arr[i]]=i+1
#         # t.append(i+1)
#     elif arr[i]==arr[i+1]:
#         d[arr[i]]=i+1
#     else:
#         pass
#     i=i+1
# print(t)

# 1331

nums = [1,1]
d={}
for i in nums:
    if i not in  d:
        d[i]=1
    else:
        d[i]+=1

t=[]
for k,v in d.items():
    if v>=2:
        t.append(k)
for i in range(1,len(nums)+1):
    if i not in nums:
        t.append(i)