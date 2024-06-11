image=[[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
# print(l)
# for i in l:
#     i.reverse()
# print(l)
# for i in l:
#     for j in range(len(i)):
#         if i[j]==0:
#             i[j]=1
#         else:
#             i[j]=0
# print(l)
def find(image):
    for i in image:
        i.reverse()
    for i in image:
        for j in range(len(i)):
            if i[j] == 0:
                i[j] = 1
            else:
                i[j] = 0
    return image
print(find(image))