#DP는 정말 모르겠다!
import sys

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if li[j] < li[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))