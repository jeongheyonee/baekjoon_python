# https://hyo-ue4study.tistory.com/235
# 쿼드트리(Quad Tree)
# 트리의 자식 노드가 4개인 트리를 뜻함
# https://tmdrl5779.tistory.com/102

# 왜 sys를 하면 런타임 에러가 나는걸까?
# 이 부분에 대해서 더 공부해보아야겠다!
# import sys의 기능에 대해서 더 공부하기!
n = int(input())

video = [list(map(int, input())) for _ in range(n)]

def dnc(x, y, n):
    check = video[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != video[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        dnc(x, y, n)  # 오른쪽 위
        dnc(x, y + n, n)  # 왼쪽 위
        dnc(x + n, y, n)  # 오른쪽 아래
        dnc(x + n, y + n, n)  # 왼쪽 아래
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


dnc(0, 0, n)
