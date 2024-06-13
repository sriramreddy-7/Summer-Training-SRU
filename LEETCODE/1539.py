nums1 = [2,4]
nums2 = [1,2]
s=set()
for i in nums1:
    if i in nums2:
        s.add(i)

print(s)
