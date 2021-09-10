import sys

input = sys.stdin.readline

n = int(input())

d = list(map(int, input().split()))
p = list(map(int, input().split()))

# # 마지막 도시가 아닌 곳에서의 기름의 최소값을 찾음
# # 그 곳에서 나머지 길이의 기름을 다 넣어야 최소 값이 될 수 있음
# # 이 전까지는 다음 도시까지의 길이만큼 넣는 것이 제일 좋음
# # 17점짜리 답안임
# m = min(p[:n-1])
# idx = p.index(m)
# cost = 0
# for i in range(idx+1):
#     if i == idx:
#         cost += sum(d[idx:]) * p[i]
#     else:
#         cost += d[i] * p[i]

# 처음 도시에서 무조건 기름을 넣어야 하기 때문에 초기값을 첫 도시의 기름 값 * 다음 도시로 가기 위한 거리
# for문을 돌면서 이전 도시와의 기름값을 계속 비교
# 더 작은 값을 기름값으로 택하여 거리를 곱하면 됨
m = p[0]
cost = d[0] * m


for i in range(1, n-1):
    m = min(m, p[i])
    cost += m * d[i]

print(cost)