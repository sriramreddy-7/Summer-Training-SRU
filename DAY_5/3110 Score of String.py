s = "zaz"
c=0
for i in range(len(s)-1):
    c=c+abs(ord(s[i])-ord(s[i+1]))
print(c)
