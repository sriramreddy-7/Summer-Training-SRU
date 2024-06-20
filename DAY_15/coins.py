def coins(c, t):
    dp = [0] * (t + 1)
    dp[0] = 1
    for i in c:
        for j in range(i, t + 1):
            dp[j] += dp[j - i]

    print(dp)
    if dp[t] > 0:
        return True
    else:
        return False


c = [2, 3, 5, 6]
t = 7
print(coins(c, t))