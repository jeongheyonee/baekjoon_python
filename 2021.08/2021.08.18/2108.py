import sys
from collections import Counter

li = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]

li.sort()
# 산술평균
print(round(sum(li)/len(li)))

# 중앙값
print(li[len(li)//2])

# 최빈값
# most_common([n]): n 개의 가장 흔한 요소와 그 개수를 가장 흔한 것부터 가장 적은 것 순으로 나열한 리스트를 반환
count_li = Counter(li).most_common()
if len(count_li) > 1 and count_li[0][1] == count_li[1][1]:
    print(count_li[1][0])
else:
    print(count_li[0][0])

# 범위
print(max(li)-min(li))