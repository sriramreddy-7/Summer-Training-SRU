# address = "1.1.1.1"
# def remove(address):
#     return address.replace(".","[.]")
#
# print(remove(address))
# s=[ chr(i) for i in range(97,123)]
# s=set(s)
# flag=set()
# # print(type(flag))
# sentence = "leetcode"
# # sentence = "thequickbrownfoxjumpsoverthelazydog"
# ns=[x for x in sentence]
# ns=set(ns)
# if ns-s==flag:
#     print(True)
# else:
#     print(False)
s=[ chr(i) for i in range(97,123)]
sentence = "leetcode"
for i in s:
    if i in sentence:
        continue
    else:
        print(False)
        break
else:
    print(True)
