# 이항계수를 어떻게 분할 정복으로 풀죠?
# https://rhdtka21.tistory.com/123
# https://kyun2da.github.io/2020/08/30/BinomialCoefficient/
# 이해를 한 번 해볼게요....
# 페르마의 소정리, 유클리드 호제법

N, K = map(int, input().split())
p = 1000000007

def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n*i)%p
    return n

def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n

    tmp = square(n, k//2)
    if k%2:
        return tmp*tmp*n%p
    else:
        return tmp*tmp%p

top = factorial(N)
bot = factorial(N-K) * factorial(K) % p

print(top*square(bot, p-2)%p)
