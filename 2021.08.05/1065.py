def sequence(n):
    n = list(range(1, n+1))
    cnt = 0
    for i in n:
        s = str(i)
        if i < 100:
            cnt += 1
        else:
            if int(s[1])-int(s[0]) == int(s[2])-int(s[1]):
                cnt += 1
    return cnt

n = int(input())
print(sequence(n))
