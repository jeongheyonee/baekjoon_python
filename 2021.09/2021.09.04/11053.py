import sys

input = sys.stdin.readline

n = int(input())

li = list(map(int, input().split()))

grow = [li[0]]

for i in range(len(li)-1):
    if li[i] < li[i+1]:
        grow.append(li[i+1]-li[i])
l = grow.index(max(grow))
print(l+1)
