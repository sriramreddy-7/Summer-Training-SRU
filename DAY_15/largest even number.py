s1='tu5g2k1h8'
s2='g5g8gd6h3'
nu=[]
for i in s1:
    if i.isdigit() and i not in nu:
        nu.append(i)
for i in s2:
    if i.isdigit() and i not in nu:
        nu.append(i)
print(nu)
a=sorted(nu)
b=a[::-1]
if int(b[-1])%2==0:
    print(''.join(b))
else:
    for i in range(len(b)-2,-1,-1):
        if int(b[i])%2==0:
            b.append(b.pop(i))
            print(''.join(b))
            break
    else:
        print(-1)