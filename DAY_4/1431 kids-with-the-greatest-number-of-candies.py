candies = [2,3,5,1,3]
extraCandies = 3
result=[]
m=max(candies)
for i in candies:
    if i+extraCandies>=m:
        result.append(True)
    else:
        result.append(False)
print(result)