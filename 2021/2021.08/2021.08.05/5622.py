s = input()

a = ['ABC', 'DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
#
# m = ""
# for i in s:
#     for j in range(len(a)):
#         for k in a[j]:
#             if i == k:
#                 m += str(2 + j)
# s = 0
# for i in m:
#     s += int(i)+1
#
# print(s)

t = 0
for i in s:
    for j in range(len(a)):
        for k in a[j]:
            if i == k:
                t += j + 3

print(t)