# nums=list(map(str,input().split(',')))
nums=['5','3.8','7','5.6','4','2','5']
fsum=0.0
esum=0
osum=0
for i in range(len(nums)):
    if '.' in nums[i]:
        fsum+=float(nums[i])
    elif '.' not in nums[i]:
        if int(nums[i])%2==0:
            esum+=int(nums[i])
        else:
            osum+=int(nums[i])
        
print(f"Floats: {fsum}\nEvens: {esum}\nOdds: {osum}")
