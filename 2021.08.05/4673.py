n = list(range(1, 10001))
a = list(range(1, 10001))

def self(n):
    for i in a:
        i = str(i)
        l = len(i)
        s = int(i)
        for j in range(l):
            s += int(i[j])
        if s in n:
            n.remove(s)

    for k in n:
        print(k)

self(n)