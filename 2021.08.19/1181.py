import sys
n = int(sys.stdin.readline())
l = []
for _ in range(n):
    w = str(sys.stdin.readline())
    l.append((w, len(w)))

l = list(set(l))

l.sort(key=lambda x:(x[1], x[0]))

for i in l:
    print(i[0], end = '')
