def count(li, left, right, a, b, sr, ss):
    if left > right:
        return sr, ss
    if a < li[left]:
        sr += 1
        a = li[left]

    if b < li[right]:
        ss += 1
        b = li[right]

    return count(li, left + 1, right - 1, a, b, sr, ss)

li = [3, 5, 9, 6, 8, 10]
left = 1
right = len(li) - 2
a = li[0]
b = li[-1]
sr = 1
ss = 1

sr, ss = count(li, left, right, a, b, sr, ss)

print(sr, ss)