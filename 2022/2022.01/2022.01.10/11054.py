# 바이토닉 수열
n = int(input())
arr = list(map(int, input().split()))
re = arr[::-1]

plus = [1 for _ in range(n)]
minus = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
            plus[i] = max(plus[i], plus[j]+1)
        if re[i] > re[j]:
            minus[i] = max(minus[i], minus[j]+1)

result = [0 for _ in range(n)]
for i in range(n):
    result[i] = plus[i] + minus[n-i-1] -1

print(max(result))
