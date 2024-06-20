ranges = [[1,1]]
left = 1
right = 50
x= [x for x in range(left,right+1)]
print(x)
k=0
for i in range(len(ranges)):
    f=0
    for j in range(len(ranges[i])):
        s=ranges[i][0]
        e=ranges[i][-1]
        print(s,e)
        if ranges[i][j] not in x:
            f=f+1
            k=k+1
    if f==len(ranges[i]):
        print(False)
        break
else:
    print(True)