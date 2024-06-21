arr = [1,2,4]
arr.sort(reverse=True)
print(arr)
cs=0
for i in range(len(arr)-1):
    if i==0:
        cs=abs(arr[i]-arr[i+1])
    else:
        if cs!=abs(arr[i]-arr[i+1]):
            print(False)
            break
else:
    print(True)