words = ["cd","ac","dc","ca","zz"]
count=0
for i in words:
    print(i[::-1])
    if i[::-1] in words:
        if words.index(i)!=words.index(i[::-1]):
            count+=1
            words.remove(i[::-1])
print(count)