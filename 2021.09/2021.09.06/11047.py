import sys

input = sys.stdin.readline

n, k = map(int, input().split())
money = []

for i in range(n):
    m = int(input())
    if k > m:
        money.append(m)
cnt = 0
for i in range(len(money)-1, -1, -1):
    while True:
        if k < money[i]:
            break
        else:
            k -= money[i]
            cnt += 1

print(cnt)