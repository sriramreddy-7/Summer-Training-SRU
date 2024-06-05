nums = [13,25,83,77]
print(nums)
# r=[]
# def s(x):
#     for j in str(x):
#         r.append(int(j))
#
# for i in nums:
#     s(i)
#
# print(r)
r=[]
def divide(x):
    y = 0
    while x>0:
        y=x%10
        r.append(y)
        x=x//10

for i in nums:
    divide(i)
print(r)

