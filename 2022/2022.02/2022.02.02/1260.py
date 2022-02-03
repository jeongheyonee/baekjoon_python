# dfs: 깊이 우선 탐색
# 최대한 깊이 내려간 뒤, 더 이상 깊이 갈 곳이 없을 경우 옆으로 이동
# bfs: 너비 우선 탐색
# 최대한 넓게 이동한 다음, 더 이상 갈 수 없을 때 아래로 이동
# 오,,,어떻게 풀어야 하는지 이것도 모르겠다!
# https://goplanit.site/42.%20Algorithm(1260_py)/ 
import sys
from collections import deque

def dfs(n):
    print(n, end = ' ')
    visit[n] = True
    for i in graph[n]:
        if not visit[i]:
            dfs(i)

def bfs(n):
    visit[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visit[i]:
                queue.append(i)
                visit[i] = True


input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()

dfs(v)

visit = [False] * (n+1)
print()
bfs(v)