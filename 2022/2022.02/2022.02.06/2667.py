# 이 문제 진지하게 어떻게 풀어야 할지 감이 안 잡힘.
# dfs, bfs로 어떻게 풀지?
# https://chancoding.tistory.com/61
# 일단 이해 안 가고 bfs로도 다시 풀어보기!

n = int(input())
map = [[0]*n for _ in range(n)]
visit = [[0]*n for _ in range(n)]

for i in range(n):
    line = input().strip()
    for j, l in enumerate(line):
        map[i][j] = int(l)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y, c):
    visit[x][y] = 1
    global nums

    if map[x][y] == 1:
        nums += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == 0 and map[nx][ny] == 1:
                dfs(nx, ny, c)

cnt = 1
nlist = []
nums = 0
for a in range(n):
    for b in range(n):
        if map[a][b] == 1 and visit[a][b] == 0:
            dfs(a, b, cnt)
            nlist.append(nums)
            nums = 0

print(len(nlist))
for n in sorted(nlist):
    print(n)
