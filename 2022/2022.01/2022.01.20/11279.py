# heap을 어떻게 사용할 것인가?
# heap 직접 구현으로 다시 풀어보기!!! 꼭!!!
# https://hooongs.tistory.com/130

import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    x = int(input())

    if x == 0:
        try:
            print(-1*heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, -x)