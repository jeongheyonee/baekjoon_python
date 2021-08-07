t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    f = [i for i in range(1, n+1)]
    for _ in range(k):
        for j in range(1, n):
            f[j] += f[j-1]
    print(f[-1])
# 2층: 1 4 10 20
# 1층: 1 3 6 10
# 0층: 1 2 3 4
