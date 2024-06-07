# words = ["$easy$","$problem$"]
# separator = "$"
# # separator = "."
# l=[]
# for i in words:
#     l.append(i.split(separator))
# print(l)
# words=[]
# for j in l:
#     for k in j:
#         words.append(k)
#
# print(words)
nums = [10,21,31]
r=0
def encrypt(x):
    rem=0
    t=[]
    while x>0:
        rem=x%10
        t.append(rem)
        x=x//10
    mt=max(t)
    for i in range(len(t)):
        t[i]=mt
    s=""
    for j in t:
        s=s+str(j)
    s=int(s)
    return s


for i in nums:
    r+=encrypt(i)

print(r)