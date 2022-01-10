import math

n, k = map(int, input().split())
# s = 1
# for i in range(k):
#     s *= (n-i)
# s2 = 1
# for i in range(k):
#     s2 *= (k-i)
# print(s//s2)

# factorial로 풀어보기
b = math.factorial(n)//(math.factorial(k) * math.factorial(n-k))
print(b)