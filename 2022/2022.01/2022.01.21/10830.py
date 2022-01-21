# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-10830-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%96%89%EB%A0%AC-%EC%A0%9C%EA%B3%B1-%EA%B3%A8%EB%93%9C4-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5
import sys

input = sys.stdin.readline

n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]


# 행렬의 곱셈
def mul(x, y):
    matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for l in range(n):
                matrix[i][j] += x[i][l] * y[l][j]
            matrix[i][j] %= 1000
    return matrix


def square(a, b):
    if b == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= 1000
        return a

    tmp = square(a, b // 2)
    if b % 2:
        return mul(mul(tmp, tmp), a)
    else:
        return mul(tmp, tmp)


result = square(a, b)
for i in result:
    print(*i)