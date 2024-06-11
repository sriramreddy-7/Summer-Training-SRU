nums = [1,100]
s=set()
while nums!=[]:
    a=min(nums)
    b=max(nums)
    avg=(a+b)/2
    s.add(avg)
    nums.remove(a)
    nums.remove(b)
print(len(s))