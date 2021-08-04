n = int(input())
m = list(map(int, input().split()))
mm = max(m)

for i in range(len(m)):
    m[i] = m[i]/mm*100

print(sum(m)/n)
