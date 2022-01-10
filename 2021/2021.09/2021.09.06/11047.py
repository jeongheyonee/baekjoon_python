# Greedy Algorithm
# 최적의 해를 구하는 상황에서 사용하는 방법
# 여러 경우 중 하나를 선택할 때 그것이 그 상황에서 가장 좋다고 생각하는 것을 선택해 나가는 방식으로 진행하여 답을 구함

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = 0

money = []

for _ in range(n):
    money.append(int(input()))
money = sorted(money, reverse=True)

for i in range(n):
    cnt = k//money[i]
    s += cnt
    k -= (cnt)*money[i]
    if k == 0:
        break
print(s)

# for i in range(n):
#     m = int(input())
#     if k > m:
#         money.append(m)
# cnt = 0
# for i in range(len(money)-1, -1, -1):
#     while True:
#         if k < money[i]:
#             break
#         else:
#             k -= money[i]
#             cnt += 1
#
# print(cnt)

