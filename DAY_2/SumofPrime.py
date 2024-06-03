def prime(n):
    for i in range(2,n-1):
        if n%i==0:
            return False
    else:
        return True
def divide(flag):
    _sum=0
    while flag>0:
        r=flag%10
        _sum=_sum+r
        flag=flag//10
    # _sum=int(_sum)
    if _sum>9:
        _sum=divide(_sum)
    print("sum",_sum)
    return _sum
        
n=int(input("Enter the Num : "))
flag=n
d=divide(flag)
r=prime(d)
if r:
    print(n)
else:
    while True:
        n=n+1
        print("n",n)
        flag=n
        print("flag",flag)
        d=divide(flag)
        r=prime(d)
        if r:
            print(n)
            break
        else:
            continue
            # print("flag, n",flag,n)
        
    
# n=input() 
#flag=sum(list(map(int,int(n))))