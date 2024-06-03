s = "is2 sentence4 This1 a3"
l = list(map(str, s.split(" ")))
r = [None] * len(l)

for i in range(len(l)):
    key = l[i]
    print("key", key)
    key = int(key[-1]) - 1
    print(key)
    r[key] = l[i][:-1]

print(r)
result = " ".join(r)
print(result)
