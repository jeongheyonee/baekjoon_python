import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    x = int(input())

    if x != 0:
        arr.append(x)
    else:
        if len(arr) == 0:
            print(0)
            continue
        print(max(arr))
        arr.remove(max(arr))