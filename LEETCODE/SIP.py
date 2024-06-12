nums = [1,3,5,6]
target = 0
i=0
j=len(nums)-1
while i<=j:
    mid=(i+j)//2
    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]<target:
            i=mid+1
    else:
        j=mid-1
if target>nums[mid]:
    print(mid+1)
else:
    print(mid)


