nums = [[1,2,3],[5,6,7],[9,10,11]]
def prime(x):
    for i in range(2,x-1):
        if x%i==0:
            return False
    else:
        return True

max=0
for i in range(len(nums)):
    for j in range(len(nums[i])):
        if i==j or i+j==len(nums)-1:
            if prime(nums[i][j]) and nums[i][j]>max:
                max=nums[i][j]

print(max)



