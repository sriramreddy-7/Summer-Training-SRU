
operations = ["--X","X++","X++"]
x = 0
for i in operations:
    if i == "--X" or i == "X--":
        x -=1
    if i == "X++" or i == "++X":
        x +=1


print(x)