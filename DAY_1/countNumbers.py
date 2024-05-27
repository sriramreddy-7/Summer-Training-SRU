a=[3,4,7,8,8,6,4,3,5]
b=[]
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(f"{i}-{a.count(i)}")