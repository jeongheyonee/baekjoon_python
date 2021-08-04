n = int(input())

for i in range(n):
    cnt = 0
    a = input()
    for j in range(len(a)):
        if a[j] == 'O':
            cnt1 = 0
            try:
                for k in range(j, a.index('X', j, len(a))):
                    cnt1 += 1
            except:
                for k in range(j, len(a)):
                    cnt += 1
            cnt += cnt1
    print(cnt)