# 진짜 어려움
# n이하의 숫자들 중 소수 찾기
def prime(n):
    s = [True] * n
    m = int(n**0.5)
    for i in range(2, m+1):
        if s[i] == True:
            for j in range(i+i, n, i):
                s[j] = False
    return [i for i in range(2, n) if s[i] == True]

# n이하의 소수들 중 합이 n
def sosu(n):
    li = prime(n)
    idx = max([i for i in range(len(li)) if li[i]<= n/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(li)):
            if li[i] + li[j] == n:
                return [li[i], li[j]]

for _ in range(int(input())):
    n = int(input())
    print(" ".join(map(str, sosu(n))))