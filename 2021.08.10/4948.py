while True:
    n = int(input())

    if n == 0:
        break

    count = 0
    for i in range(n+1, 2*n+1):
        cnt = 0
        for j in range(2, i+1):
            if i%j == 0:
                cnt += 1
                if cnt > 2:
                    break
        if cnt == 2:
            count += 1
    print(count)
