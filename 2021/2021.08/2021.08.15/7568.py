n = int(input())

li = []
for i in range(n):
    li.append(list(map(int, input().split())))

for i in range(n):
    k = 0
    for j in range(n):
        if li[i][0] < li[j][0]:
            if li[i][1] < li[j][1]:
                k += 1
    print(k+1, end=' ')