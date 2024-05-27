a="11"
b="1"
f1=a
f2=b
a=int(a)
b=int(b)
a_bin=0
b_bin=0
for i in range(len(f1)-1,-1):
    print(i)
    for j in f1:
        print(j)
        a_bin=a_bin+((2**(i))*int(j))
print("a_bin",a_bin)


        