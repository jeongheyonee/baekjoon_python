import sys

input = sys.stdin.readline

n = int(input())
nge = list(map(int, input().split()))
result = [-1] * n

for i in range(n):
    if i == n-1:
        break
    for j in range(i+1, n):
        if nge[i] < nge[j]:
            result[i] = nge[j]
            break

print(*result)