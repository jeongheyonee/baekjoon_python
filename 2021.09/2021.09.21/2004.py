from math import factorial

n, m = map(int, input().split())
c = factorial(n) // (factorial(n-m) * factorial(m))
cnt = 0
c = str(c)
for i in range(len(c)-1, -1, -1):
    if c[i] == '0':
        cnt += 1
    if c[i] != '0':
        break

print(cnt)

