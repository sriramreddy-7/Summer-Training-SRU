# nums=[1,2,3,4,5]
# n=len(nums)
# for i in range(n-1):
#     print(f"[{i}] [{nums[i]},{nums[i+1]}]")

# print(word.find('A'))
# s=[chr(i) for i in range(97,123)]
# l=[chr(i) for i in range(65,91)]
# s=s+l
# print(s)
word = "aaAbcBC"
# word = "abc"
c=0
for i in range(len(word)):
    if word.find(chr(ord(word[i])+32)):
        c=c+1
print(c)
# s=[chr(i) for i in range(97,123)]
# for i in s:





