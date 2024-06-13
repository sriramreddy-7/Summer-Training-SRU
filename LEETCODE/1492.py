n = 4
k = 4
l=[i for i in range(1,n+1) if n%i==0]
try:
    print(l[k-1])
except:
    print(-1)