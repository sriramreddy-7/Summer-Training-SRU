a=[3,8,5,4,3]
b=[5,8,9,3,2]
c=tuple()
def _sum(i,s1,s2):
    if i==len(a):
        return s1,s2
    if(a[i]%2==0):
        s1+=a[i]
    if b[i]%2!=0:
        s2+=b[i]
    return _sum(i+1,s1,s2)
x,y=_sum(0,0,0)
print(x,y)


