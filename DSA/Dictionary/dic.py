n=int(input())
d={}
for i in range(n):
    data=list(map(str,input().split(" ")))
    d[data[0]]=data[1:]
    data=[]
find=input()
r=d.get(find)
s=0
s=float(0)
for i in range(len(r)):
    r[i]=int(r[i])
    s=s+r[i]
f=1
if s/3==f:
    print()

