import math

t = int(input())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    # 두 원이 동심원이면서 반지름 동일
    if d==0 and r1==r2:
        print(-1)
    # 내접 or 외접
    elif abs(r1-r2) == d or r1+r2 == d:
        print(1)
    # 두 원이 서로 다른 두 점에서 만날 때
    elif abs(r1-r2) < d < (r1+r2):
        print(2)
    # 그 외의 경우
    else:
        print(0)