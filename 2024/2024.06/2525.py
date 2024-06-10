def timer(n, t):
    n = n.split()
    n = [int(i) for i in n]
    n[1] = n[1] + t
    if n[1] >= 60:
        n[1] = n[1] % 60
        n[0] += n[1] // 60
    return str(n[0]) + " " + str(n[1])

print(timer("14 30", 20))


