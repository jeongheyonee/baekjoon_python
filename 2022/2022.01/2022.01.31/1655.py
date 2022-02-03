# 음,,,,어떻게 풀어야 하는 건지...
# heap을 어떻게 쓰면 될지...
import heapq
import sys

input = sys.stdin.readline

n = int(input())

leftHeap = []
rightHeap = []

for _ in range(n):
    x = int(input())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -x)
    else:
        heapq.heappush(rightHeap, x)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftV = heapq.heappop(leftHeap)
        rightV = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightV)
        heapq.heappush(rightHeap, -leftV)

    print(-leftHeap[0])