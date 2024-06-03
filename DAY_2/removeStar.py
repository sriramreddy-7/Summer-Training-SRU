s="leet**cod*e"
l=list(map(str,s))
stack=[]
for i in range(len(s)):
    if s[i]!="*":
        stack.append(s[i])
    else:
        if stack:
            stack.pop()
r="".join(stack)
print(r)
