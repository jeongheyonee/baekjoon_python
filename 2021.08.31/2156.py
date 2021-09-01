import sys

input = sys.stdin.readline

n = int(input())    #포도주 잔의 개수

w = [0]
for _ in range(n):
    w.append(int(input()))

dp = [0]
dp.append(w[1])

if n > 1:
    dp.append(w[1] + w[2])
for i in range(3, n + 1):
    dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))

print(dp[n])