# 문제의 규칙을 찾기가 어려움
import math

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    d = y-x     #x와 y의 거리
    cnt = 0

    n = math.floor(math.sqrt(d))
    n_square = n**2     #정수를 제곱근으로 갖는 제곱수(ex. 9: 9의 제곱근 => 3)

    if d == n_square:
        cnt = (n*2)-1
    elif n_square < d <= n_square + n:
        cnt = n*2
    elif (n_square + n) < d:
        cnt = n*2 + 1
    elif d < 4:
        cnt = d

    print(cnt)

# math.floor: 내림 기능
# x보다 작거나 같은 가장 큰 정수인 x의 바닥값(floor)을 반환합니다.
# x가 float가 아니면, x.__floor__()에 위임하고, 이것은 Integral 값을 반환해야 합니다.


