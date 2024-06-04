words = ["abc","bcd","aaaa","cbc"]
x = "a"
result=[]
for i in range(len(words)):
    for j in words[i]:
        if x in j:
            result.append(i)
            break
print(result)