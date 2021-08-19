import sys
l = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

l.sort(key=lambda x:(x[1], x[0]))

for i in l:
    print(i[0], i[1])
