# n=[4,8,14,22,36,68]
n=[14,16,20,22]
def prime(start,end):
    l=[]
    for j in range(start,end+1):
        f=0
        for k in range(2,j-1):
            if j%k==0:
                f=1
                break
        if f==0:
            l.append(j)
    if l!=[]:
        return max(l)
    return 0

s=[]
for i in range(len(n)-1):
    r=prime(n[i],n[i+1])
    s.append(r)
