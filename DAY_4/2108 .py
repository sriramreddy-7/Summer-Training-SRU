words = ["abc","car","ada","racecar","cool"]
for i in words:
    if i==i[::-1]:
        print(True)
        break
else:
    print("")