nums1 = [1,3]
nums2 = [2,4]
nums1=nums1+nums2
nums1.sort()
if len(nums1)%2==0:
    print(nums1[len(nums1)//2],nums1[(len(nums1)//(2))-1])
    f=(nums1[len(nums1)//2]+nums1[(len(nums1)//(2))-1])/2
    print(f)
else:
    print(nums1[len(nums1)//2])