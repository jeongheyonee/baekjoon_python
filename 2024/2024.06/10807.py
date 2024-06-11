n = int(input())    # n개의 정수
list = input().split()
v = input()
s = 0
for i in list:
    if i == v:
        s += 1
print(s)