import sys
from collections import deque


def dfs(n):
    global cnt
    visit[n] = True
    for i in computer[n]:
        if not visit[i]:
            cnt+=1
            dfs(i)
    return cnt

def bfs(n):
    global cnt
    visit[n] = True
    queue = deque([n])
    while queue:
        v = queue.popleft()
        for i in computer[v]:
            if not visit[i]:
                queue.append(i)
                cnt += 1
                visit[i] = True
    return cnt

input = sys.stdin.readline

n = int(input())    #컴퓨터의 수
m = int(input())    #컴퓨터 쌍의 수

computer = [[] for _ in range(n+1)]
visit = [False] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

for i in range(1, n+1):
    computer[i].sort()

print(dfs(1))

# bfs로 풀어보기
visit = [False] * (n+1)
cnt = 0
print()
print(bfs(1))