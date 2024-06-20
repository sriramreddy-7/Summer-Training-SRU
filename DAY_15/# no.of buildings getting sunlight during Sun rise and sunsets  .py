li=[3,5,9,6,8,10]

left=1
right=len(li)-1

sr=1
ss=1

a=li[0]
b=li[right]

while left<len(li) and right>=0:
    if a<li[left]:
        sr+=1
        a=li[left]
        left+=1
    else:
        left+=1
    if b<li[right]:
        ss+=1
        b=li[right]
        right-=1
    else:
        right-=1
print(sr,ss)
