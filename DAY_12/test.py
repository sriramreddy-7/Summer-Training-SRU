# a="apple a day"
# s=a[-1:-5:-1]
# print(s)
def fun(x):
    if(x == 1):
        return 1
    print(x)
    fun(x-1)
    print(x)
a=4
fun(a)