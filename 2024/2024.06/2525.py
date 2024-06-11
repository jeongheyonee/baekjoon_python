n = input()
n = n.split()
t = int(input())

n = [int(i) for i in n]
n[1] = n[1] + t
if n[1] >= 60:
    n[0] += (n[1] // 60)
    if n[0] >= 24:
        n[0] -= 24
    n[1] = n[1] % 60
print(n[0], n[1])