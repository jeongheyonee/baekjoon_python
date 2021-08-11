import math

def postulate(n):
    prime = [True for _ in range(2*n+1)]
    prime[0] = False    # 1은 소수가 아님
    prime[1] = False
    for i in range(2, int(math.sqrt(2*n))+1):
        if prime[i] == True:
            j = 2
            while i*j <= n:
                prime[i*j] = False
                j += 1
    cnt = 0
    for i in range(n, 2*n+1):
        if i > 1:
            if prime[i] == True:
                cnt += 1
    return prime

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(postulate(n))