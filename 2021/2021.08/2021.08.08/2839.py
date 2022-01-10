n = int(input())

s = 0
while n>=0:
    if n%5 == 0:
        s += n//5
        print(s)
        break
    n -= 3
    s += 1
else:
    print(-1)



# n1 = n//5
# n2 = n%5
# n3 = n2//3
# n4 = n//3
#
# s = n1
#
# if n2%3==0:
#     s += n3
#
# else:
#     if n%3 == 0:
#         s = n4
#     else:
#         s = -1
# print(s)