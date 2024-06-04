hours=[0,1,2,3,4]
target=2
count=0
for i in range(len(hours)):
    if hours[i]>=target:
        count=count+1
print(count)
