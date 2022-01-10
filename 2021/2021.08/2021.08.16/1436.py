# n = int(input())
#
# print(666 + 1000*(n-1))
# 위 코드가 틀린 이유: N번째 영화의 제목은 세상의 종말 (N번째로 작은 종말의 숫자) 와 같다.
# 666100 인 경우 667번째가 아니라는 이야기!

n = int(input())
x = 666
cnt = 0

while True:
    if '666' in str(x):
        cnt += 1
    if cnt == n:
        print(x)
        break
    x += 1
