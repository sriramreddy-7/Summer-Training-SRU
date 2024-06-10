# print(l)
# l=[chr(i) for i in range(97,123)]
s="a b c d e f g h i j k l m n o p q r s t u v w x y z"
# for i in l:
#     if i not in s:
#         print(False)
#         break
# else:
#     print(True)
d={}
for i in s:
    if i not in d and i.isalpha():
        d[i]=1
c=0
print(d)
for k,v in d.items():
    c=c+v
if c==26:
    print(True)
else:
    print(False)



