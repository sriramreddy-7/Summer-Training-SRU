arr = ["aaa","aa","a"]
k = 1
c=0
s=set()
for i in arr:
    if i not in s:
        s.add(i)
    else:
        c=c+1
        if c>1:
            print(i)
if k<len(arr):
    print("")
else:
    print(arr[0])
