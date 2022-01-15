# https://it-garden.tistory.com/288


import sys
input = lambda : sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    dq = input()[1:-1].split(',')
    p = p.replace('RR', '')

    r = 0
    f, b = 0, 0

    for i in p:
        if i == 'R':
            r += 1
        elif i == 'D':
            if r%2 == 0:
                f += 1
            else:
                b += 1

    if f + b <= n:
        dq = dq[f:n-b]

        if r%2 == 1:
            print('['+','.join(dq[::-1])+']')
        else:
            print('['+','.join(dq)+']')
    else:
        print('error')