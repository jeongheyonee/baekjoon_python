# https://my-coding-notes.tistory.com/102
import sys

input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

card.sort()

def bs(num, bound):
    start, end = 0, n
    while(start < end):
        mid = (start + end) // 2
        if bound == 0:
            if card[mid] < num:
                start = mid + 1
            else:
                end = mid
        else:
            if card[mid] <= num:
                start = mid + 1
            else:
                end = mid
    return end

answer = []

for i in find:
    answer.append(bs(i,1) - bs(i,0))
print(*answer)