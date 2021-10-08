from math import gcd, sqrt

n = int(input())
li = [int(input()) for _ in range(n)]
li.sort()

iv = []
result = []

for i in range(1, n):
    iv.append(li[i] - li[i-1])

prev = iv[0]

for i in range(1, len(iv)):
    prev = gcd(prev, iv[i])

for i in range(2, int(sqrt(prev))+1):
    if prev % i == 0:
        result.append(i)
        result.append(prev//i)

result.append(prev)
result = list(set(result))
result.sort()
print(*result)