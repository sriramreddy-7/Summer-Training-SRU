# num = 38
# def divide(num):
#     rem=0
#     sm=0
#     while(num>0):
#         rem=num%10
#         sm=sm+rem
#         num=num//10
#     if sm>9:
#         return divide(sm)
#     if sm<=9:
#         return sm
#
#
# r=divide(num)
# print("outside",r)
# nums1 = [1,1,3,2]
# nums2 = [2,3]
# nums3 = [3]
# nums1=set(nums1)
# nums2=set(nums2)
# nums3=set(nums3)
# nums1=nums1.intersection(nums2,nums3)
#
# print(nums1,nums2,nums3)

arr = ["d","b","c","b","c","a"]
k = 2
d={}
for i in arr:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1
# for k,v in d.items():
#      print(k,v)
print("----------------")
c=1
for key,v in d.items():
    if v==1:
        print("c,k",c,k)
        if c==k:
            print(key)
            break
        else:
            print("bc",c)
            c=c+1
            print("ac",c)
            print("3")
    else:
        print("4")

# for k,v in d.items():
#     print(k,v)