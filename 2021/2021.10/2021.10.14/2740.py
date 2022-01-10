n, m = map(int, input().split())

a = []
b = []
for _ in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())

for _ in range(m):
    b.append(list(map(int, input().split())))

result = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += a[i][l] * b[l][j]

for i in result:
    print(*i)
