s = "abccbaacz"
print(s)
# for i in range(len(s)-1):
#     print(s[i],s[i+1])
#     if s[i]==s[i+1]:
#         print(s[i])
#         break
d=set()
for i in s:
    if i not in d:
        d.add(i)
    else:
        print(i)
        break
