nums=[5,4,2,3]
rep=len(nums)//2
print(rep)
r=[]
for i in range(rep):
    alice=min(nums)
    nums.remove(alice)
    bob=min(nums)
    nums.remove(bob)
    r.append(bob)
    r.append(alice)
print(r)


