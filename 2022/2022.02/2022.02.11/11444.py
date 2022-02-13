# 피보나치를 재귀가 아닌 분할정복으로?
# n번째 피보나치 수를 구해서 1000000007로 나눈 나머지 출력
# ? 아 진짜 어떻게 풀어....?
# 행렬 제곱 -> 피보나치!
# https://my-coding-notes.tistory.com/97
# https://claude-u.tistory.com/406
# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-11444-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98-%EC%88%98-6-%EA%B3%A8%EB%93%9C3-%EB%B6%84%ED%95%A0-%EC%A0%95%EB%B3%B5

import sys

input = sys.stdin.readline

n = int(input())
p = 1000000007


def mul(x, y):
    n = len(x)  #왜 동일하게 n으로 해야하는가? m과 같은 다른 변수로 설정하면 백준에서 메모리 초과 뜸!
    matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            e = 0
            for l in range(n):
                e += x[i][l] * y[l][j]
            matrix[i][j] = e % p
    return matrix


def square(a, b):
    if b == 1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] %= p
        return a

    tmp = square(a, b // 2)
    if b % 2:
        return mul(mul(tmp, tmp), a)
    else:
        return mul(tmp, tmp)


fib = [[1,1], [1,0]]
print(square(fib, n)[0][1])