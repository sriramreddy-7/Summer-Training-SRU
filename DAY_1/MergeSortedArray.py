# arr1=list(map(int,input().split(',')))
# arr2=list(map(int,input().split(',')))
arr1=[1,5,8,9]
arr2=[2,7,9,10,14]
i=0
j=0
# while i>=0 and j<len(arr2):
#     if arr1[i]>arr2[j]:
#         arr1[i],arr2[j]=arr2[j],arr1[i]
#         i=i-1
#         j=j+1
#     else:
#         j += 1


# print(arr1+arr2)
c=[]
while(i<len(arr1) and j<len(arr2)):
    if arr1[i]<arr2[j]:
        c.append(arr1[i])
        i=i+1
    if arr1[i]>arr2[j]:
        c.append(arr2[i])
        j=j+1
if (i<len(arr1)):
    c.extend(arr1[i:])
if (j<len(arr2)):
    c.extend(arr2[j:])

print(c)
        
    


