def search(x, li):
    s = 0
    l = set(li)
    for i in l:
        if x in i:
            s += 1
    if s != 0:
        return s
    print(li)
    return False


n = int(input())
li = []
s = ''

for i in range(n):

    s = input()

    if int(s[0]) == 1:
        li.append(s[2:])

    elif int(s[0]) == 2:
        if s[2:] in li:
            print("True")
        else:
            print("False")

    elif int(s[0]) == 3:
        print(search(s[2:], li))

    elif int(s[0]) == 4:
        se = list(set(li))
        li = se.copy()
        for i in li:
            if i == s[2:]:
                li.remove(i)
        print(li)