def happy(n):
    rem=0
    s=0
    while n>0:
        rem=n%10
        s=s+rem**2
        n=n//10
    print("s",s)
    if s<4:
        return s
    else:
        return happy(s)

n=int(input())
r=happy(n)
print("r",r)
if r==1:
    print(True)
else:
    print(False)


