import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

people = deque([i for i in range(1, n+1)])
result = []

while len(people) > 0:
    # print("origin", people)
    people.rotate(-k)
    # print(people)
    result.append(str(people[-1]))
    people.pop()

print('<'+', '.join(result)+'>')