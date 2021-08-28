n = int(input())
s = [int(input()) for _ in range(n)]

if n == 1:
    print(s[0])
else:
    dp = [0] * (n+1)
    dp[1] = s[0]
    dp[2] = s[0] + s[1]

    for i in range(3, n+1):
        dp[i] = max(dp[i-3]+s[i-2]+s[i-1], dp[i-2]+s[i-1])

    print(dp[n])
