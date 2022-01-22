import sys

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))
answer = [0] * m

for i in range(m):
    answer[i] = card.count(find[i])


for j in answer:
    print(j, end=' ')