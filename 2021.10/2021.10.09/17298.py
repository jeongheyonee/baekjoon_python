# https://hongcoding.tistory.com/40

import sys

input = sys.stdin.readline

n = int(input())
nge = list(map(int, input().split()))
result = [-1] * n
stack = []

stack.append(0)
for i in range(1, n):
    while stack and nge[stack[-1]] < nge[i]:
        result[stack.pop()] = nge[i]
    stack.append(i)

print(*result)