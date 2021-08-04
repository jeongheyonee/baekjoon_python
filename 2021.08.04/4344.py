c = int(input())

for i in range(c):
    n = list(map(int, input().split()))

    sum = 0
    for j in range(1, len(n)):
        sum += n[j]
    avg = sum / n[0]

    cnt = 0
    for k in range(1, len(n)):
        if n[k] > avg:
            cnt += 1
    p = cnt/n[0] * 100
    print('{:.3f}'.format(p)+'%')