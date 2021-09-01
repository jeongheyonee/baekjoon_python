# n = 옮기려는 원반의 개수
# from_p = 원반의 출발점
# to_p = 도착점
# aux_p = 보조
def hanoi(n, from_p, to_p, aux_p):
    if n == 1:
        print(from_p, to_p)
        return

    # 원반 n-1개를 aux_p로 이동
    hanoi(n-1, from_p, aux_p, to_p)
    # 가장 큰 원반을 도착점으로 이동
    print(from_p, to_p)
    hanoi(n-1, aux_p, to_p, from_p)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)