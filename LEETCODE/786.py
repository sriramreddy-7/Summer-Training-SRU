# arr = [1, 2, 3, 5]
# k = 3
# s=[]
# for i in range(len(arr)):
#     for j in range(i,len(arr)):
#         if arr[i]<arr[j]:
#             s.append(arr[i]/arr[j])
# s.sort()
# print(s)
# s = "   fly me   to   the moon  "
s = "   fly me   to   the moon  "
l = list(s.split(" "))
d={}
for i in l:
    if i not in d:
        d[i]=len(i)
print(l)
print(d)
c=0
for k,v in d.items():
    print(k)
    if k!="":
        print(c,len(k))
        c=len(k)
# print(c)


