n = int(input())
cnt = 1
plus = 6
room = 1

if n == 1:
    print(1)

else:
    while True:
        cnt += plus
        room += 1
        if n <= cnt:
            print(room)
            break
        plus += 6