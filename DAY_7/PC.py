l=[2,2,5,56,8,9,6,3,3,4]
# for i in range(len(l)):
#     for j in range(len(l)):
#         for k in range(len(l)):
#             print(l[i],l[j],l[k])

def c(l,k):
    def fun(curr,start):
        if len(curr)==k:
            print(curr)
            return
        for i in range(start,len(l)):
            fun(curr+[l[i]],i+1)
        return
    fun([],0)
a=[3,5,1,6]
k=3
c(a,k)

