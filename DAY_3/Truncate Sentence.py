class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=list(map(str,s.split(" ")))
        print(l)
        st=""
        sp=" "
        for i in range(k):
            if i==0:
                st = st+"".join(l[i])
                print("i",st)
            else:
                st=st+sp+"".join(l[i])
                print(st)
        return st

obj = Solution()
print(obj.truncateSentence("Hello how are you Contestant",4))