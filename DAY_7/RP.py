# word = "abcdefd"
# word = "xyxzxe"
# ch = "z"
# s=""
# for i in word:
#     if i==ch:
#         i=word.index(ch)
#         s=word[:i+1][::-1]+word[i+1:]
#         print(s)
#         break
# else:
#     print(word)
# s = "l|*e*et|c**o|*de|"
# count=0
# f=0
# for i in s:
#    if  i== "|":
#        f=1


# s = ["h","e","l","l","o"]
# i=0
# j=len(s)-1
# while i<=j:
#     s[i],s[j]=s[j],s[i]
#     i=i+1
#     j=j-1
# print(s)

# word1="ab"
# word2="pqrs"
# s=""
# i=0
# j=0
# n = max(len(word1), len(word2))
#
# while i < n:
#     if i < len(word1):
#         s += word1[i]
#     if i < len(word2):
#         s += word2[i]
#     i += 1
# print(s)
# while i<len(word1) and j<len(word2):
#         s=s+word1[i]
#         s=s+word2[j]
#         print(s)
#         i+=1
#         j+=1
# while i<len(word1):
#     s=s+word2[i]
#     i+=1
#
# while j<len(word2):
#     s=s+word2[j]
#     print(s)
#     j+=1
# s = "aaabbb"
# r1="qwertyuiop"
# r2="asdfghjkl"
# r3="zxcvbnm"
# words = ["Hello","Alaska","Dad","Peace"]
# r=[]
# for i in words:
#     print(i.lower())
#     if i.lower() in r1 or i.lower() in r2 or i.lower() in r3:
#         r.append(i)
# print(r)


# nums = [1,1,1,3,3,4,3,2,4,2]
# d={}
# for i in nums:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# for k,v in d.items():
#     if v>=2:
#         print(True)
#         break
# else:
#     print(False)

# s="is2 sentence4 This1 a3"
# l=list(map(str,s.split(" ")))
# d=[0]*(len(l)+1)
# for i in l:
#     if i not in d:
#         k=int(i[-1])
#         i=i.replace(str(k),"")
#         d[k]=i
# d.remove(0)
#
# r=" ".join(d)
# print(r)
# a=[chr(i) for i in range(97,123)]
# print(a)
# s = "a1c1e1"
# def shift(c,x):
#
#
# for j in range(len(s)-1):
#     if j%2==0:
# words = ["one.two.three","four.five","six"]
#
# separator = "."
# words = ["$easy$","$problem$"]
# separator = "$"
words = ["#,"]
separator = "#"
# r=",".join(words)
# r=r.replace(separator,",")
# print(r)
# words=[]
# words=list(map(str,r.split(",")))
# s=[]
# for i in words:
#     if i!="":
#         s.append(i)
# print(s)
r=separator.join(words)
s=r.split(separator)








