nums = [1,0,1,1]
k = 1
d={}
for i in range(0,len(nums)):
    if nums[i] not in d:
        d[nums[i]]=i
    else:
        # print(f"{d[nums[i]]}-{i}")
        if abs(d[nums[i]]-i)<=k:
            print(True)
            break
        else:
            d[nums[i]]=i
    print(f"{d[nums[i]]}-{i}")
    # print(d)
else:
    print(False)