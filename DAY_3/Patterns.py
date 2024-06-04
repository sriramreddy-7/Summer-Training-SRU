n=int(input("enter size:"))
c=1
for i in range(1,n+1):
    for j in range(n):
        if i==1 or i==n:
            print("*",end=" ")
        else:
            if j in [1,2,3]:
                print(c,end=" ")
                c+=1
            else:
                print("*",end=" ")
    print("")

