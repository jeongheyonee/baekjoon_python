n, m = map(int, input().split())

s = []

def backtracking():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if i not in s:
            s.append(i)
            backtracking()
            s.pop()

backtracking()

# itertools 사용 가능
from itertools import permutations
p = permutations(range(1, n+1), m)
for i in p:
    print(' '.join(map(str, i)))
