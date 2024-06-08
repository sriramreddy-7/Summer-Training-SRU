a=int(input())
def isprime(x):
    if x==1:
        return 1
    if x==2:
        return 1
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1
for i in range(1,(a//2)+1):
    if (isprime(i) and isprime(a-i)):
        print("Yes")
        break
else:
    print("No")