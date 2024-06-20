
s = "(]"
stack=[]
ob=["{","[","("]
cb=["}","]",")"]
for i in range(len(s)):
    if s[i] in ob:
        stack.insert(0,s[i])
    elif s[i] in cb and stack==[]:
        print(False)
    elif s[i] in cb and cb.index(s[i])==ob.index(stack[0]):
        stack.pop(0)
    else:
        if s[i] in cb and cb.index(s[i])!=ob.index(stack[0]):
            print(False)
else:
    print(True)



