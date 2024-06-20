s = "r"
f=set()
for j in s:
    if j.islower():
        if j.upper() in s:
            f.add(j)
    else:
        if j.lower() in s and j.upper() not in f:
            f.add(j)

if f:
    print(max(f).upper())
else:
    print("")
