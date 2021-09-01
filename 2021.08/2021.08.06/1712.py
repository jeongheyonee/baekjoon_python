a, b, c = map(int, input().split())

if b >= c:
    print(-1)
else:
    print((a//(c-b))+1)
    # A+B*n = C*n
    # 이런 이유로 3행에서 b >=c 인 경우에 구할 수 없음
    # A = C*n - B*n
    # A = n(C-B)
    # n = A/(C-B)