a, b, c = map(int, input().split())

# 무조건 시간초과가 날 코드
for i in range(b):
    a *= a

print(a%c)