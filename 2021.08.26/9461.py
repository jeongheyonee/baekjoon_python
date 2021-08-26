import sys

input=sys.stdin.readline
t = int(input())

# for _ in range(t):
#     k = [1, 1, 1]
#     n = int(input())
#     if n<4:
#         k[n-1]
#     for i in range(3, n):
#         k.append(k[i-3] + k[i-2])
#     print(k[n-1])

k = [1, 1, 1]
n = [int(input()) for _ in range(t)]
for i in range(3, max(n)):
    k.append(k[i-3]+k[i-2])

for i in n:
    print(k[i-1])