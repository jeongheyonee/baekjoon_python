import math

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    print(math.lcm(a, b))

# 유클리드 호제법을 이용하여서도 구할 수 있음