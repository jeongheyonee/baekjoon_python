n = int(input())

l = []

for _ in range(n):
    l.append(int(input()))

# 버블정렬: 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
# m = 0
# for i in range(n):
#     for j in range(i+1, n):
#         if l[i] > l[j]:
#             m = l[i]
#             l[i] = l[j]
#             l[j] = m

# 삽입정렬: 2번째 원소부터 시작하여 그 앞(왼쪽)의 원소들과 비교하여 삽입할 위치를 지정한 후, 원소를 뒤로 옮기고 지정된 자리에 자료를 삽입
for i in range(1, len(l)):
    while (i>0) & (l[i] < l[i-1]):
        l[i], l[i-1] = l[i-1], l[i]

        i-=1

for i in range(n):
    print(l[i])
