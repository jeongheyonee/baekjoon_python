import sys

def dfs(n):
    global cnt
    visit[n] = True
    for i in computer[n]:
        if not visit[i]:
            cnt+=1
            dfs(i)
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