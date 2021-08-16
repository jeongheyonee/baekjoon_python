# 문제가 이해가 잘 안된다...
# 어렵다..ㅠㅜ
n, m = map(int, input().split())
org = []
mini = []

for _ in range(n):
    org.append(input())

for i in range(n-7):
    for j in range(m-7):
        idx1 = 0
        idx2 = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if(l+k)%2 == 0:
                    if org[k][l] != 'W':
                        idx1 += 1
                    if org[k][l] != 'B':
                        idx2 += 1
                else:
                    if org[k][l] != 'B':
                        idx1 += 1
                    if org[k][l] != 'W':
                        idx2 += 1
        mini.append(idx1)
        mini.append(idx2)

print(min(mini))