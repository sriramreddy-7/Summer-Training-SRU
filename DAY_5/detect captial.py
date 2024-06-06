# word = "USA"
# if word.isupper():
#     print(True)
# if word.islower():
#     print(False)
# if word.istitle():
#     print(True)
# else:
#     print(False)

# word = "aaAbcBC"
# c=0
# i=0
# n=len(word)
# # for i in range(len(word)-1):
# d={}
# for i in range(n):
#     if
#     d[word[i]]=True

# nums=[1,15,6,3]
# s=sum(nums)
# c=0
# def digit_sum(x):
#     r=0
#     flag=0
#     while x>0:
#         r=x%10
#         flag=flag+r
#         x=x//10
#     print(flag)
#     return flag
# for i in nums:
#     # print(digit_sum(i))
#     c=c+digit_sum(i)
# print(s,c)
# print(abs(s-c))

nums = [1,2,2,1]
k = 1
c=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if abs(nums[i]-nums[j])==k:
            c=c+1
print(c)




