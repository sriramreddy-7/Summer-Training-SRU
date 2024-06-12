# s="hello:5438,car:214,book:8799,apple:2187"
st=list(map(str,input().split(",")))
d={}
for i in range(len(st)):
    r=st[i].split(":")
    d[r[0]]=int(r[1])
emp=""
for k,v in d.items():
    length=len(k)
    ep=list(map(int,str(v)))
    print(ep)
    if length in ep:
        emp = emp + str(k)[length - 1]
        print(emp)
    else:
        while length != 0:
            if length in ep:
                emp = emp + str(k)[length - 1]
                print(emp)
                break
            else:
                length -= 1
        if length==0:
            emp=emp+"x"
            print(emp)
print(emp)

# for i in range(len(ep)):
        #     print("length",length)
        #     length = length - 1
        #     if ep[i]==length:
        #         print("flength",length)
        #         emp = emp + str(k)[length - 1]
        #         print(emp)
        #         break

            # else:
            #     length=length-1