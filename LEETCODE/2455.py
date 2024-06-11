nums=[1,3,6,10,12,15]
avg=[]
for i in nums:
    if i%2==0 and i%3==0:
        avg.append(i)

print(sum(avg)/len(avg))


