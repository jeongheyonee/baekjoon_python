t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    cnt = 0
    for j in range(1, w+1):
        for k in range(1, h+1):
            cnt += 1
            if cnt == n:
                print('{:d}'.format(k)+'{:02d}'.format(j))
                # 한 자리의 호실일 경우에 0을 추가하여 자릿수를 맞춤