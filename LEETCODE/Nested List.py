# N=int(input())
# f=[]
# N=2*N
# while N>0:
#     name=input()
#     score=float(input())
#     f.append([name,score])
#     N=N-2
# print(f)
# def solve(s):
#     x=""
#     for i in s:
#         if i.islower():
#             x=x+i.upper()
#         elif i.isupper():
#             x=x+i.lower()
#         else:
#             x=x+i
#     return x
#
# s="HackerRank.com presents"
# print(solve(s))
#
M=int(input())
a=set(map(int,input().split(" ")))
n=int(input())
b=set(map(int,input().split(" ")))
c=a-b
d=b-a
c=c.union(d)
c=list(c)
c.sort()
for i in c:
    print(i)