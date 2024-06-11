# s = "abcd"
# t = "abcde"
# ds={}
# for i in s:
#     if i not in ds:
#         ds[i]=1
#     else:
#         ds[i]+=1
# dt={}
# for i in t:
#     if i not in dt:
#         dt[i]=1
#     else:
#         dt[i]+=1
#
# print(ds)
# print(dt)
l=[[1,1,0],[1,0,1],[0,0,0]]
print(l)
for i in l:
    i.reverse()
print(l)
for i in l:
    for j in range(len(i)):
        if i[j]==0:
            i[j]=1
        else:
            i[j]=0
print(l)