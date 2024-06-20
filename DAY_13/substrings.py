s1 = 'abcd'
s2 = 'axbdc'
s = ""
m = []
for i in range(len(s1) + 1):
    l = [0] * (len(s2) + 1)
    m.append(l)
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):
        if s1[i - 1] == s2[j - 1]:
            m[i][j] = m[i - 1][j - 1] + 1
        else:
            m[i][j] = max(m[i][j - 1], m[i - 1][j])

s = ''
while (i != 0 and j != 0):
    if s1[i - 1] == s2[j - 1]:
        s = s + s1[i - 1]
        i = i - 1
        j = j - 1
    else:
        if m[i][j] == m[i - 1][j]:
            i = i - 1
        else:
            j = j - 1
print(s)
print(m[len(s1)][len(s2)])
print(m[len(s1)][len(s2)])