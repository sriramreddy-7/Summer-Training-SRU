words1 =["leetcode","is","amazing","as","is"]
words2 =["amazing","leetcode","is"]
d={}
def check(w1,w2):
    for i in words1:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    c=0
    for j in words2:
        for k,v in d.items():
            if j==k and v==1:
                c=c+1
    return c
if len(words1)>len(words2):
    print(check(words1,words2))
else:
    print(check(words2,words2))