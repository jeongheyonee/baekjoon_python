n = int(input())
s = 0
for i in range(1, n+1):
    li = list(map(int, str(i)))
    s = i + sum(li)
    if s == n:
        print(i)
        break
    if i==n:
        print(0)