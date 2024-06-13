# st="1C0C1C1A0B1"
st="0C1A1B1C1C1B0A0"
s=""
n=len(st)
i=1
j=0
while n>1:
    r=0
    if st[i]=="A":
        r=int(st[j])&int(st[j+2])
    if st[i]=="B":
        r=int(st[j])|int(st[j+2])
    if st[i]=="C":
        r=int(st[j])^int(st[j+2])
    i = i + 2
    j = j + 2
    n=n-2
print(r)