import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
deque = deque([])

for _ in range(n):
    word = input().split()
    order = word[0]

    if order == 'push_front':
        value = word[1]
        deque.appendleft(value)

    elif order == 'push_back':
        value = word[1]
        deque.append(value)

    elif order == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.popleft())

    elif order == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())

    elif order == 'size':
        print(len(deque))

    elif order == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])

    elif order == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])