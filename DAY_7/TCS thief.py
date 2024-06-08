def rec(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return max(l)
    left=l[0]+rec(l[2:])
    right=l[1]+rec(l[3:])
    return max(left,right)
li=[13,9,4,10,5,7]
print(rec(li))