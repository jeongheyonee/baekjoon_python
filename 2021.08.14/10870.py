fibo = [0, 1]

n = int(input())

for i in range(2, n+1):
    m = fibo[i-1] + fibo[i-2]
    fibo.append(m)

print(fibo[n])
