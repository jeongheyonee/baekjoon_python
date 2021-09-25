# '(', ')' 의 개수가 동일해야 한다는 점을 이용
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    ps = list(input())
    s = 0

    for i in ps:
        if i == '(':
            s += 1
        elif i == ')':
            s -= 1
        if s < 0:
            print('NO')
            break

    if s == 0:
        print('YES')
    elif s > 0:
        print('NO')