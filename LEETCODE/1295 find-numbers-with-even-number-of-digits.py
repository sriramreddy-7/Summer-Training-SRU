nums=[12,345,2,6,7896]
count=0
def count_nums(n):
    r=0
    c=0
    while n>0:
        r=n%10
        c=c+1
        print("n,c",n,c)
        n=n//10

    if c%2==0:
        return 1
    return 0

for n in nums:
    result=count_nums(n)
    print("result",result)
    count+=result

print(count)
