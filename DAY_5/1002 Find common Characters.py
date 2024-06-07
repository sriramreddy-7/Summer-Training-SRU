# words = ["bella","label","roller"]
# words = ["are","amy","u"]
# left = 0
# right = 2
words = ["hey","aeo","mu","ooo","artro"]
left = 1
right = 4
c=0
for i in range(left,right+1):
   if words[i][0] in ['a','e','i','o','u'] and words[i][-1] in ['a','e','i','o','u']:
       print(words[i][0],words[i][-1])
       print(words[i])
       c=c+1
print(c)