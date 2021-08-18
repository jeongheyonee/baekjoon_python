n = int(input())

l = []

for _ in range(n):
    l.append(int(input()))

m = 0
for i in range(n):
    for j in range(i+1, n):
        if l[i] > l[j]:
            m = l[i]
            l[i] = l[j]
            l[j] = m

for i in range(n):
    print(l[i])