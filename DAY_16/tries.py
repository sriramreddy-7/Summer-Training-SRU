class node:
    def __init__(self):
        self.d = {}
        self.flag = 0


class tries:
    def __init__(self):
        self.root = node()

    def insert(self, str):
        t = self.root
        for i in str:
            if i not in t.d:
                t.d[i] = node()
            else:
                t.d[i]
        t.flag = 1

    def search(self, str):
        t = self.root
        for i in str:
            if i not in t.d:
                return False
            t = t.d[i]
            return True

    def search_prefix(self, s):
        t = self.root
        for i in s:
            if i not in t.d:
                return False
            t = t.d[i]
        return True

    def sugg(self, str):
        def fun(t, s):
            if t.flag == 1:
                print(s)
                return
            for i in t.d:
                fun(t.d[i], s + i)

        t = self.root
        s = ''
        for i in str:
            if i in t.d:
                s = s + i
                t = t.d[i]
            else:
                return
        fun(t, s)

    def longest_prefix(self):
        def fun(t, s):
            if t.flag == 1:
                prefix_list.append(s)
            for i in t.d:
                fun(t.d[i], s + i)

        prefix_list = []
        fun(self.root, "")
        return max(prefix_list, key=len)


t1 = tries()
n = int(input())
for i in range(n):
    a, s = input().split()
    if a == '1':
        t1.insert(s)
    if a == '2':
        print(t1.search(s))
    if a == '3':
        print(t1.search_prefix(s))
    if a == '4':
        print(t1.sugg(s))
    if a == '5':
        print(t1.longest_prefix(s))

