import sys

t = int(input())

for i in range(t):
    n1, n2 = map(int, sys.stdin.readline().split())
    print(n1+n2)
