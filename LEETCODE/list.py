n=int(input())
nums=[]
while n:
    l=list(map(str,input().split(" ")))
    if l[0]=="append":
        nums.append(int(l[1]))
    elif l[0]=="insert":
        nums.insert(int(l[1]),int(l[2]))
    elif l[0]=="print":
        print(nums)
    elif l[0]=="remove":
        nums.remove(int(l[1]))
    elif l[0]=="sort":
        nums.sort()
    elif l[0]=="pop":
        nums.pop()
    else:
        if l[0]=="reverse":
            nums.reverse()
    n=n-1

