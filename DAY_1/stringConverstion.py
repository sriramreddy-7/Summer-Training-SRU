st=input("Enter a string: ")
r=""
for i in range(len(st)):
    if st[i] in ['a','e','i','o','u']:
        r=r+st[i].upper()
    if st[i] not in ['a','e','i','o','u']:
        r=r+st[i].lower()
    else:
        continue
print(r) 