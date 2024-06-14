d={
    5:[7,3],7:[5,3,4],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]
}
# d={
#     5:[7,3,1],7:[5,3,4,2],4:[7,8,2,3],8:[3,4,2,6,5],3:[5,7,8,5],2:[4,8,8]
# }
# v=[]
# q=[]
# for k,v in d.items():
#     q.append(k)
#     break
# print(q)
#
# for k,v in d.items():
#     for j in v:
#         if j not in q:
#             q.append(j)
#         break
#
# print(q)
def bfs(d,n):
    v=[]
    q=[n]
    while (q):
        for i in d[q[0]]:
            if i not in q and i not in v:
                q.append(i)
        print(q)
        v.append(q.pop(0))
        print(v)
        print(v[-1])
bfs(d,next(iter(d)))







