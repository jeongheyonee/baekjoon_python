import sys
l = [list(map(int, sys.stdin.readline().split())) for _ in range(int(sys.stdin.readline()))]

# 시간초과
# for i in range(len(l)):
#     for j in range(i+1, len(l)):
#         if l[i][0] > l[j][0]:
#             l[i], l[j] = l[j], l[i]
#         elif l[i][0] == l[j][0]:
#             if l[i][1] > l[j][1]:
#                 l[i], l[j] = l[j], l[i]

l.sort(key=lambda x:(x[0], x[1]))

for i in l:
    print(i[0], i[1])
