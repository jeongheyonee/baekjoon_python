# 에라토스테네스의 체 이용! -> 시간복잡도 -> sqrt
import math

m, n = map(int, input().split())

prime = [True for _ in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if prime[i] == True:
        j = 2
        while i*j <= n:
            prime[i*j] = False
            j += 1

for i in range(m, n+1):
    if i>1:
        if prime[i] == True:
            print(i)

# # for i in prime:
# #     cnt = 0
# #     for j in range(1, i+1):
# #         if i%j == 0:
#             cnt += 1
#             if cnt > 2:
#                 break
#     if cnt == 2:
#         print(i)
#         try:
#             for k in range(prime.index(i)+1, len(prime)+1):
#                 if prime[k] % i == 0:
#                     prime.remove(prime[k])
#         except:
#             continue
#
# print(prime)