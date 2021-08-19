import sys
n = int(sys.stdin.readline())
l = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    l.append((i, int(age), name))

l.sort(key=lambda x:(x[1], x[0]))

for i in l:
    print(i[1], i[2])