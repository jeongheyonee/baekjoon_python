import sys

input = sys.stdin.readline

n = int(input())

A = list(map(int, input().split()))

m = int(input())

M = list(map(int, input().split()))

for i in M:
    if i in A:
        print(1)
    else:
        print(0)