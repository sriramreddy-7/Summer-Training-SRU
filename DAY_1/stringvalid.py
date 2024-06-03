n="hmd4u3@"
u,l,s,d=0,0,0,0
for i in range(len(n)):
    if n[i].isupper():
        u=1
    elif n[i].islower():
        l=1
    elif n[i].isdigit():
        d=1
    else:
        s=1

m=4-(u+l+s+d)
if (len(n)+m)<8:
    print(8-len(n))
    
else:
    print(m)