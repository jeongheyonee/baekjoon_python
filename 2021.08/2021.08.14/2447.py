import sys
sys.setrecursionlimit(10**6)    #10^6으로 최대 재귀 깊이 설정

def star(l):
    if l == 1:
        return['*']

    Stars = star(l//3)
    L = []

    for s in Stars:
        L.append(s*3)
    for s in Stars:
        L.append(s+' '*(l//3)+s)
    for s in Stars:
        L.append(s*3)
    return L

n = int(sys.stdin.readline().strip())
print('\n'.join(star(n)))

# sys.stdin.readline(): 입력함수, 한 줄에 여러 입력 값을 받을 수 있음