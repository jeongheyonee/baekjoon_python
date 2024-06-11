x = int(input())    # 영수증에 적힌 총 금액 x
n = int(input())    # 영수증에 적힌 구매한 물건 종류의 수
list = []
s = 0
for i in range(n):
    list.append(input().split())
    s += int(list[i][0]) * int(list[i][1])

if s == x:
    print("Yes")
else:
    print("No")