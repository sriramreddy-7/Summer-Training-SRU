# sentence = "i am tired"
# searchWord = "you"
# l=list(map(str,sentence.split(" ")))
# for i in range(len(l)):
#     if len(l[i])>=len(searchWord):
#         if searchWord==l[i][:len(searchWord)]:
#             print(i)
#             break
# else:
#     print(-1)

# words = ["leetcode","win","loops","success"]
# pref = "code"
# c=0
# for i in range(len(words)):
#     if words[i]>=pref:
#         if pref==words[i][0:len(pref)]:
#             c=c+1
# print(c)
"""for i in range(len(haystack)):
    c=0
    k=i
    j=0
    while j<=n and k<=len(haystack):
        print(haystack[k],needle[j])
        if needle[j]==haystack[k]:
            c=c+1
        else:
            break
        print("b",j,k)
        j=j+1
        print("j",j)
        k=k+1
        print("a",j,k)
    if c==len(needle):
        print(i)
        break
else:
    print(-1)"""
# haystack = "hello"
# needle = "ll"
# k=0
# if len(needle)>len(haystack):
#     print(-1)
# n=len(needle)
# for i in range(len(haystack)):
#     print(i,n,haystack[i:n])
#     if haystack[i:i+n]==needle:
#         print(i)
#         break
# else:
#     print(-1)
# sequence = "a"
# word = "a"
# n=len(word)
# ns=len(sequence)
# k=0
# i=0
# while i<ns:
#     if sequence[i:i+n]==word:
#         print("indices",i,i+n)
#         k=k+1
#         i=i+n
#     else:
#         i=i+1

"""aaaba 0-5
aaaba 5-10
aaba
aaaba
aaaba
aaaba
aaaba
"""
# s = "textbook"
# vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
#
# s1=s[:len(s)//2]
# s2=s[len(s)//2:]
# if s1==s2:
#     print(False)
# else:
#     c=0
#     k=0
#     for i in s1:
#         if i in vowels:
#             c=c+1
#     for j in s2:
#         if j in vowels:
#             k=k+1
#     if c==k:
#         print(True)
#     else:
#         print(False)

# words =["feh","w","w","lwd","c","s","vk","zwlv","n","w","sw","qrd","w","w","mqe","w","w","w","gb","w","qy","xs","br","w","rypg","wh","g","w","w","fh","w","w","sccy"]
# s ="w"
# count=0
# for i in range(len(words)):
#     if words[i][0]==s[0] or words[i]==s:
#         count+=1
#         print(f"{words[i]}-{count}")
# print(count)

# num = "1210"
# l=list(map(int,num))
# print(l)
# def check():
#     pass
#
#
# for i in l:
#     pass


strs = ["1","01","001","0001"]
l=[]

def check(x):
    try:
        x=int(x)
        return x
    except:
        if x.isalpha() or x.isalnum():
            return len(x)
        if x.isnumeric():
            return int(x)

for i in strs:
    l.append(check(i))

print(max(l))
