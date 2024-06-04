size=int(input("enter size :"))
m=[]
for i in range(size):
    m.append(input())
print(m)
s=input("enter string :")
flag=0
for i in range(len(s)):
    if s[i] in m[i]:
        continue
    else:
        flag=1
        break
if flag==1:
    print("No")
else:
    print("yes")

