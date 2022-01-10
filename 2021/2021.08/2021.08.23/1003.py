import sys
input = sys.stdin.readline
t = int(input())

# 시간초과
# 호출 회수에 대한 생각을 다시 해볼 것
# def fibo(n):
#     if n == 0:
#         cnt[0] += 1
#         return 0
#     elif n == 1:
#         cnt[1] += 1
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
#
# for i in range(t):
#     n = int(input())
#     cnt = [0, 0]
#     fibo(n)
#     print(cnt[0], cnt[1])

z = [1, 0, 1]
o = [0, 1, 1]

def fibo(n):
    l = len(z)
    if l <= n:
        for i in range(l, n+1):
            z.append(z[i-1]+z[i-2])
            o.append(o[i-1]+o[i-2])
    print(z[n], o[n])

for i in range(t):
    fibo(int(input()))