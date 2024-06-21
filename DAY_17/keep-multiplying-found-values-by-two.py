nums = [2]
original=2

def find(key):
    if original in nums:
        return 2*original
    else:
        return False

for i in range(len(nums)+1):
    r=find(original)
    if r!=False:
        original=r
        # print(original)
    else:
        print(original)
        break





