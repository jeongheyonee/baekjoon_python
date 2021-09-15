import math

n = int(input())

li = list(map(int, input().split()))

for i in range(1, n):
    gcd = math.gcd(li[0], li[i])
    print(f'{li[0]//gcd}/{li[i]//gcd}')