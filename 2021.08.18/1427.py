n = list(map(int, str(input())))

n = sorted(n, reverse=True)

for i in n:
    print(i, end='')