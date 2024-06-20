# sequence ="aaabaaaabaaabaaaabaaaabaaaabaaaaba"
# word = "aaaba"
sequence ="ababc"
word ="ac"
count=0
nw=len(word)
ns=len(sequence)
d=[]
for i in range(ns):
    d.append([i,sequence[i]])
print(d)
print("--")
i=0
r=[]
k=0
while i<ns:
    if sequence[i:i+nw]==word:
        print(f"[{i},{i+nw}]")
        count+=1
        i=i+nw
    elif sequence[i-1:i-1+nw]==word:
        k=k+1
        i = i + nw
    else:
        i=i+1
    print(i)
print(count)
print(k)

# aaaba
# aaaba
# aaba
# aaaba
# aaaba
# aaaba
# aaaba
