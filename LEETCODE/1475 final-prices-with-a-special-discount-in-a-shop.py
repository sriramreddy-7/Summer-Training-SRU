# prices = [8,4,6,2,3]
# r=[]
# for i in range(len(prices)):
#
operations = ["--X","X++","X++"]
x = 0
for i in operations:
    if i == "--X":
        x = x + --x
    if i == "X++":
        x = x + x++
    if i == "++X":
        x = x + ++x
    if i == "X--":
        x = x + x--
print(x)