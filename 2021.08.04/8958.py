n = int(input())

for i in range(n):
    cnt = 0
    a = input()
    for j in a:
        if j == 'O':
            cnt1 = 0
            for k in range(a.index(j), a.index('X')+1):
                cnt1 += 1
            cnt += cnt1
    print(cnt)