from collections import Counter

n1 = int(input())   # 의상 수

for _ in range(n1):
    n2 = int(input())   # 의상 종류
    li = []
    for i in range(n2):
        name, type = input().split()
        li.append(type)
    num = 1
    r = Counter(li)

    for k in r:
        num *= r[k] + 1
    print(num -1)


