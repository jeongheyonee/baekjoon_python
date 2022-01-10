import sys

input = sys.stdin.readline

n = int(input())

time = list(map(int, input().split()))

time.sort()

s = 0

for i in range(len(time)):
    s += sum(time[:i+1])

print(s)