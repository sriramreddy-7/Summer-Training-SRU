nums=[1,3,5,6]
target=5
start=0
end=len(nums)-1
while start<=end:
    mid=(start+end)//2
    if nums[mid]==target:
        print(nums.index(target))
        break
    elif target>nums[mid]:
        start=mid+1
    elif target<nums[mid]:
        end=mid+1


