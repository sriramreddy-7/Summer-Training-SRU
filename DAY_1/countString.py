_str="aaabbaaaaddd"
print(f"Length {len(_str)}")
i=0
count=1
c=""
flag=[]
while i<len(_str)-1:
    if _str[i]==_str[i+1]:
        count+=1
        i+=1
        print(f"{i} in if")
    elif _str[i]!=_str[i+1]:
        # c=_str[i]+str(_str.count(_str[i]))
        flag.append(_str[i])
        flag.append(count)
        count=1
        # print(c)
        i+=1
        print(f"{i} in else")
print(flag)
        

    