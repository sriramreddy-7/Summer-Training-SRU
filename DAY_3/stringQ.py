# s=input()
# target=int(input())
# final_string=""
# for i in s:
#     r=ord(i)
#     r=int(r)
#     r=r-target
#     r=chr(r)
#     final_string=final_string+r
# print(final_string)
# print(chr(ord('a')))
a="bvec"
b=30
c=b%26
d=""
for i in a:
    if(((ord(i))-c)>=97):
        d=d+chr((ord(i))-c)
    else:
        d=d+chr(ord(i)-c+26)
print(d)

