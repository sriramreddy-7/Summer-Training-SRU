s1 = "this apple is sweet"
s2 = "this apple is sour"

l=list(map(str,(s1+" "+s2).split(" ")))
d={}
for i in l:
    if  i not in d:
        d[i]=1
    else:
        d[i]+=1
r=[]
for k,v in d.items():
    if v==1:
        r.append(k)
