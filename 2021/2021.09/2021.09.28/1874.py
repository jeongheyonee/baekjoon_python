# 이해를 더 해보아야 겠다...
# https://wook-2124.tistory.com/44077
n = int(input())

stack = []
result = []
cnt = 0
possible = True

for _ in range(n):
    num = int(input())

    while cnt < num:
        cnt += 1
        stack.append(cnt)
        result.append("+")

    top = stack[-1]
    if top == num:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break

if possible == False:
    print("NO")
else:
    for i in result:
        print(i)