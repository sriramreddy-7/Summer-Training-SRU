# month = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
#          "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
# date = "6th Jun 1933"
# l=list(date.split(" "))
# print(l)
# d=month.get(l[1])
# l[0]=l[0].replace("th","")
# l[0]=int(l[0])
# if d<10 and l[0]<10:
#     print(f"{l[2]}-{0}{d}-{0}{l[0]}")
# elif d<10:
#     print(f"{l[2]}-{0}{d}-{l[0]}")
# elif l[0]<10:
#     print(f"{l[2]}-{d}-{0}{l[0]}")
# else:
#     print(f"{l[2]}-{d}-{l[0]}")

# l=["20th"]
# i = l[0][-2] + [0]l[-1]
# if i in r:
#     l[0] = l[0].replace(i, "")
# l[0] = int(l[0])

# n = 10
#
# def guess(i):
#     pick = 6
#     if i>pick:
#         return -1
#     elif i<pick:
#         return 1
#     else:
#         if i==pick:
#             return 0

# for i in range(1,n):
#     r=guess(i)
#     if r==0:
#         print(i)
#         break
# i=1
# j=n
# while i<=j:
#     mid=(i+j)//2
#     r=guess(mid)
#     if r==0:
#         print(mid)
#         break
#     elif r==-1:
#         j=mid-1
#     else:
#         if r==1:
#             i=mid+1
# function_id = 1
# z = 5
# # Output: [[1,4],[2,3],[3,2],[4,1]]
# m=[]

n="00000010100101000001111010011100"
n=n[::-1]
r=int(n,2)
print(r)
