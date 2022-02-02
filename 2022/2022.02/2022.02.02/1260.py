# dfs: 깊이 우선 탐색
# 최대한 깊이 내려간 뒤, 더 이상 깊이 갈 곳이 없을 경우 옆으로 이동
# bfs: 너비 우선 탐색
# 최대한 넓게 이동한 다음, 더 이상 갈 수 없을 때 아래로 이동
# 오,,,어떻게 풀어야 하는지 이것도 모르겠다!

n, m, v = map(int, input().split())

for _ in range(m):
    a, b = map(int, input().split())