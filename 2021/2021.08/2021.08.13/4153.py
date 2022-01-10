import math
while True:
    l = list(map(int, input().split()))

    if l == [0, 0, 0]:
        break

    max_l = max(l)
    a = 0

    for i in l:
        if i < max_l:
            a += i**2

    if math.sqrt(a) == max_l:
        print("right")
    else:
        print("wrong")