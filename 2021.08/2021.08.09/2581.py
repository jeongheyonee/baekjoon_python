m = int(input())
n = int(input())

dec = []
for i in range(m, n+1):
    cnt = 0
    for j in range(1, i+1):
        if i%j == 0:
            cnt += 1
            if cnt > 2:
                break
    if cnt == 2:
        dec.append(i)
if len(dec) == 0:
    print(-1)
else:
    print(sum(dec))
    print(min(dec))