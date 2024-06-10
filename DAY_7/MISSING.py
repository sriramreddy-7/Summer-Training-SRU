# nums = [3,4,-1,1]
# # mx=max(nums)
# # mx=mx+1
# ht=[]
# for i in nums:
#     ht.insert(i,nums.count(i))
# print(ht)
arr = [-3,0,1,-3,1,1,1,-3,10,0]
# arr = [1,2]
d={}
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
l=[]
print(d)
c=0
for k,v in d.items():
    if v>c:
        c=v
    if c==v:
        print("c","v",c,v)
        print(False)
        break
else:
    print(True)