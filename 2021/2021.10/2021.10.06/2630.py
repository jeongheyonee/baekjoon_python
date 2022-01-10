import sys

input = sys.stdin.readline

n = int(input())

s = [list(map(int, input().split())) for _ in range(n)]
b = 0
w = 0

def cut(x, y, n):
    global b, w
    check = s[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != s[i][j]:
                cut(x, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    if check == 0:
        w += 1
        return
    else:
        b += 1
        return

cut(0, 0, n)
print(w)
print(b)