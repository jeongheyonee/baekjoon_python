import sys

input = sys.stdin.readline

n = int(input())

time = []

for _ in range(n):
    time.append(list(map(int, input().split())))
#시작시간과 종료시간으로 정렬
time.sort(key=lambda x:(x[1], x[0]))

cnt = 0
end = 0

for i, j in time:
    if i >= end:
        cnt += 1
        end = j

print(cnt)