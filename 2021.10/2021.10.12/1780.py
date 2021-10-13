# https://tmdrl5779.tistory.com/103

n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]

one = 0
zero = 0
minus = 0

def dnc(x, y, n):
    global one, zero, minus

    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:
                check = -2
                break

    if check == -2:
        n //= 3
        dnc(x, y, n)
        dnc(x, y + n, n)
        dnc(x, y + 2 * n, n)
        dnc(x + n, y, n)
        dnc(x + n, y + n, n)
        dnc(x + n, y + 2 * n, n)
        dnc(x + 2 * n, y, n)
        dnc(x + 2 * n, y + n, n)
        dnc(x + 2 * n, y + 2 * n, n)

    elif check == 1:
        one += 1
    elif check == 0:
        zero += 1
    else:
        minus += 1

dnc(0, 0, n)
print(minus)
print(zero)
print(one)