n = int(input())
m1 = n
cnt = 0
while True:
    n1 = n//10
    n2 = n%10
    n3 = n1 + n2
    n = n2*10 + n3%10
    cnt += 1

    if m1 == n:
        break

print(cnt)