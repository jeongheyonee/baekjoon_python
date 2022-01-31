# 음,,,,어떻게 풀어야 하는 건지...
# heap을 어떻게 쓰면 될지...
import heapq

n = int(input())
heap = []

for _ in range(n):
    x = int(input())
    heapq.heappush(heap, (x, x))
    print(heap)
    l = len(heap) // 2 - 1

    if len(heap)%2 == 0:
        if heap[l-1] > heap[l]:
            mid = heap[l]
        else:
            mid = heap[l-1]

    print(mid)