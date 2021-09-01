import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
o = list(map(int, input().split())) #+, -, x, //

def dfs(cnt, r, p, m, mul, div):
    global max_r
    global min_r
    if cnt == n:
        max_r = max(max_r, r)
        min_r = min(min_r, r)
        return
    if p:
        dfs(cnt+1, r+li[cnt], p-1, m, mul, div)
    if m:
        dfs(cnt+1, r-li[cnt], p, m-1, mul, div)
    if mul:
        dfs(cnt+1, r*li[cnt], p, m, mul-1, div)
    if div:
        dfs(cnt+1, -(-r//li[cnt]) if r< 0 else r//li[cnt], p, m, mul, div-1)

max_r = -1000000001
min_r = 1000000001
dfs(1, li[0], o[0], o[1], o[2], o[3])
print(max_r)
print(min_r)