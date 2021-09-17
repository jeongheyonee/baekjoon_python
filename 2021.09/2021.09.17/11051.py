from math import factorial

n, k = map(int, input().split())

b = factorial(n) // (factorial(n-k)*factorial(k))

print(b%10007)