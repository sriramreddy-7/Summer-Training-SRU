r=set()
# for i in nums:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
#     print(d[i])
#     if d[i]>=k:
#         r.add(i)
# print(d)
# if r==set():
#     for k,v in d.items():
#         if v==1:
#             r.add(k)
# print(list(r))
#1323
# nums = [3,0,1,0]
# k = 1
# d={}
# for i in nums:
#     if i not in d:j
#         d[i]=1
#     else:
#         d[i]+=1
# r=[]
# max=d[0]
# for k,v in d.items():
#     if max>=d[k]:
#         pass


# nums = [1, 3, -1, -3, 5, 3, 6, 7]
#
# k = 3
# print(nums)
# r=[]
# for i in range(len(nums)-k+1):
#     r.append(max(nums[i:i+k]))
# print(r)

def fact(n):
    print("HI")
    if n==1:
        return 1
    else:
        # print("Hi")
        return fact(n-1)*n


print(fact(5))
