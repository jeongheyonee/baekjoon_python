# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%EA%B3%B1%EC%85%88-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython

import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())

# 무조건 시간초과가 날 코드
# for i in range(b):
#     a *= a
#
# print(a%c)

# 분할정복(Divide And Conquer)으로 풀어야 시간초과를 해결할 수 있음


def dnc(a, b):
    if b == 1:
        return a%c
    temp = dnc(a, b//2)

    if b%2 == 0:
        return temp * temp %c

    else:
        return temp * temp *a % c

print(dnc(a, b))