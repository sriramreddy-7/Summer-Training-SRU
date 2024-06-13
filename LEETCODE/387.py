s = "leetcode"
c=0
d={}
# for i in range(len(s)):
#     c=s.count(s[i])
#     if c==1:
#         print(i)
#         break
# else:
#     print(-1)
for i in range(len(s)):
    if s[i] not in d:
        d[s[i]]=i
    else:
        d[s[i]]=-1
print(d)
for k,v in d.items():
    if v!=-1:
        print(v)
        break
else:
    print(-1)