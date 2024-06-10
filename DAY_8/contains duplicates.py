l=[2,3,1,3,4,2,3]
d={}
m=[]
c=0
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
c=0
while(c!=len(l)):
    r=[]
    for i in d:
        if d[i]!=0:
            d[i]=d[i]-1
            c=c+1
            r.append(i)
    m.append(r)
print(m)

