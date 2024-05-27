_str="aaabbaaaaddd"
i=0
count=1
flag=[]
r=""
while i<len(_str)-1:
    if _str[i]==_str[i+1]:
        count+=1
        i+=1
        if i==len(_str)-1:
            r=r+_str[i]+str(count)
    else:
        r=r+_str[i]+str(count)
        count=1
        i+=1
print(r)
        

    