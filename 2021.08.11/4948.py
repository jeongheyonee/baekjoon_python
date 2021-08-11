import math

# while True:
# 시간초과임...
#     n = int(input())
#
#     if n == 0:
#         break
#
#     cnt = 0
#
#     for i in range(n+1, 2*n+1):
#         if i == 1:
#             continue
#         elif i == 2:
#             cnt += 1
#             continue
#         else:
#             for j in range(2, int(math.sqrt(i))+1):
#                 if i%j == 0:
#                     break
#             else:
#                 cnt += 1
#     print(cnt)

def postulate(n):
    prime = [True for _ in range(2*n+1)]
    prime[0] = False    # 1은 소수가 아님
    prime[1] = False
    for i in range(2, int(math.sqrt(2*n))+1):
        if prime[i] == True:
            j = 2
            while i*j <= 2*n:
                prime[i*j] = False
                j += 1
    return [i for i in range(n+1, 2*n+1) if prime[i] == True]

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(len(postulate(n)))