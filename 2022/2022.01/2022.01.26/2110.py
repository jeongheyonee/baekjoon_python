import sys

input = sys.stdin.readline

n, c = map(int, input().split())

home = [int(input()) for _ in range(n)]

home.sort()

start, end = 1, home[-1] - home[0]

while start <= end:
    mid = (start + end) // 2
    old = home[0]
    cnt = 1
    for i in home:
        if i >= old+mid:
            cnt += 1
            old = i

    if cnt >= c:
        start = mid + 1

    else:
        end = mid - 1

print(end)