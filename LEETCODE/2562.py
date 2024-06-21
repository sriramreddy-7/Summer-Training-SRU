# nums = [7,52,2,4]
nums = [90,47,14,9,63,18,51,15,50,24,86,30,44,51,13,91,95,52,50,99]
def add(a,b):
    r=int(str(a)+str(b))
    return r

f=[]
c=0
while nums!=[]:
    a,b=nums[0],nums[-1]
    if nums.index(a)!=nums.index(b) or len(nums)>2:
        nums.pop(0)
        nums.pop(-1)
        f.append(add(a, b))
    elif nums.index(a)==nums.index(b) and len(nums)==2:
            nums.pop(0)
            nums.pop(-1)
            f.append(add(a, b))
    else :
        if len(nums)<=1:
            nums.pop(0)
            f.append(a)
    print(nums)
    c=c+1
    if c==25:
        break
print(sum(f))