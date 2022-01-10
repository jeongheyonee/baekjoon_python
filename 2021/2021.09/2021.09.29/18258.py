# queue: stack의 반대 개념
# FIFO(First Input First Out)
#  먼저 들어간 데이터가 먼저 나오는 구조
#  순서를 보장하기 위한 처리가 필요할 때 사용
#  저장된 요소는 순서대로 존재하고, 가장 앞에 있을 수록, 오래 기다리고 있음을 의미
import sys

input = sys.stdin.readline

n = int(input())
queue = []

for _ in range(n):
    word = input().split()
    order = word[0]

    if order == 'push':
        value = word[1]
        queue.append(value)

    elif order == 'pop':
        if len(queue)== 0:
            print(-1)
        else:
            print(queue.pop(0))

    elif order == 'size':
        print(len(queue))

    elif order == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif order == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    
    elif order == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])