num = 30003
k = 3
count=0
n=str(num)
i=0
while i<len(n):
    r=n[i:i+k]
    print(i,i+k)
    r=int(r)
    if r!=0 and num%r==0:
        count+=1
    i=i+k
print(count)

