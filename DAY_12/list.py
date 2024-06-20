n=[6,3,2,9,4,7]
m=[8,7,5,3,6,9]
# using the for loop
# r=[]
# def fun(n,m):
#     for i in range(len(n)):
#         if n[i]%2==0:
#             for j in range(len(m)):
#                 if m[j]%2!=0:
#                     r.append(n[i]+m[j])
#     return r
#
# print(fun(n,m))

# using the while loop
# def rec(n,m):
# #     i=0
# #     r=[]
# #     while i<len(n):
# #         if n[i]%2==0:
# #             j=0
# #             while j<len(m):
# #                 if m[j]%2!=0:
# #                     r.append(n[i]+m[j])
# #                 j=j+1
# #         i=i+1
# #     return r
# #
# # print(rec(n,m))

def rec(n,m):
    i=0
    r=[]
    final=[]
    while i<len(n):
        if n[i]%2==0:
            j=0
            while j<len(m):
                if m[j]%2!=0:
                    r.append(n[i]+m[j])
                j=j+1
            result=sum(r)
            final.append(result)
            r = []
        i=i+1
    return final

print(rec(n,m))