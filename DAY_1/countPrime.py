# num="7854"
# count=0
# for i in num:
#     flag=0
#     for j in range(2,int(i)):
#         if j%2==0:
#             flag=1
#             break
#     if flag==0:
#         count+=1
        
# print(count)

n=int(input("Enter Number:"))
count=0
while(n):
    if (n%20 in [2,3,5,7]):
        count+=1
    n=n//10
print(count)        
        