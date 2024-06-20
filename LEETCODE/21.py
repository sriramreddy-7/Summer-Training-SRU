# list1 = [1,2,4]
# list2 = [1,3,4]
# l1=len(list1)
# l2=len(list2)
#
# new=[]
# i=0
# if l1>l2:
#     while l2!=0:
#         if l1[i]>l2[i]:
#             new.append(l[i])

# m=0
# accounts = [[1,2,3],[3,2,1]]
# for i in accounts:
#     print(sum(i))
#     if m<sum(i):
#         m=sum(i)
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

# mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]

# s=0
# n=len(mat[0])
# for i in range(len(mat)):
#     for j in range(len(mat[i])):
#         print(j,n)
#         if i==j or j==n-1:
#             print(i,j)
#             s=s+mat[i][j]
#     n=n-1

# grid = [[1,2,4],[3,3,1]]
# f=[]
# m=0
# c=0
# while grid!=[]:
#        for i in grid:
#               if max(i)
#
#                      i.remove(c)
#                      if c>m:
#                             m=c
#
#               except:
#                      pass
#        print("grid",grid)
#        print("f",f)
#        f.append(m)
# print(sum(f))

nums = [4,3,2,7,8,2,3,1]
# n=len(nums)
# ht=[0]*(n+1)
# for i in nums:
#        ht[i]=nums.count(i)
#
# r=[]
# # n=len(nums)
# for i in range(len(ht)):
#        if i!=0 and ht[i]==0:
#               r.append(i)
#
# print(r)
#
#
# x=[i for i in range(min(nums),max(nums)+1)]
# print(x)
# nums=list(nums)
# r=[]
# for i in x:
#        if i not in nums:
#               r.append(i)
# print(r)

# grid = [[1, 2, 4], [3, 3, 1]]
# grid=[[10]]
# n=len(grid[0])
# m=0
# s=0
# c=0
# while n:
#        for i in grid:
#               c=max(i)
#               i.remove(c)
#               if c>m:
#                      m=c
#        s=s+m
#        m=0
#        n=n-1
# print(s)
# for i in grid:
#        i.remove(max(i))
#
# print(grid)
#
# for i in grid:
#        i.remove(max(i))
#
# print(grid)
matrix = [[1,2,3],[4,5,6]]
m=[]

for i in range(len(matrix[0])):
       r=[]
       for j in range(len(matrix)):
              r.append(False)
       m.append(r)
print(m)
for i in range(len(matrix[0])):
       for j in range(len(matrix[i])):
              if i!=j and m[i][j] == False and m[j][i]==False:
                     matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                     m[i][j]=True
                     m[j][i]=True
for k in matrix:
       print(k)




