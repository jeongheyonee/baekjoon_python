n = int(input())
line = []

for _ in range(n):
    line.append(list(map(int, input().split())))

line.sort(key = lambda x:x[0])

# 교차하지 않으려면 증가하는 숫자 필요
dp = [0] * n
for i in range(n):
    m = 0
    for j in range(i):
        if line[i][1] > line[j][1]:
            if m < dp[j]:
                m = dp[j]
    dp[i] = m+1

print(n-max(dp))