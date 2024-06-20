def bfs(x):
    d={5:9999,1:9999,3:9999,2:9999}
    d[x]=0
    v=[]
    q=[x]
    while (q):
        x=q[0]
        for i in g[x]:
            if i[0] not in v:
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]
        v.append(q.pop(0))

d={5:[7,3],7:[5,4,3],8:[3,4,2],3:[5,7,8],2:[4,8]}
bfs(d,next(iter(d)))

