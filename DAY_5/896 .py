nums = [1,2,2,3]
f1=1
f2=1
for i in range(len(nums)-1):
    if nums[i]<=nums[i+1]:
        f1=1
    else:
        f1=0
        break

for j in range(len(nums)-1):
    if nums[j]>=nums[j+1]:
        f2=1
    else:
        f2=0
        break

if f1==0 and f2==0:
    print(False)
else:
    print(True)
