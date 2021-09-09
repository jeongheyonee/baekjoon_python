# -(minus)기준으로 다 묶어주면 되는 거 아닐까란 생각
import sys

input = sys.stdin.readline

math = input().split('-')

n = []

for i in math:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    n.append(cnt)
num = n[0]

for i in range(1, len(n)):
    num -= n[i]
print(num)

#풀다가 split이 막혀서 참고하게 되 링크
#https://pacific-ocean.tistory.com/228