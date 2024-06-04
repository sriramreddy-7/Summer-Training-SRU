sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
count=0
cc=0
for i in range(len(sentences)):
    cc=0
    cc=sentences[i].count(" ")
    if cc>count:
        count=cc
print(count+1)
