import sys
n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))

l_sort = sorted(list(set(l)))

dic = {l_sort[i] : i for i in range(len(l_sort))}

for i in l:
    print(dic[i], end = ' ')