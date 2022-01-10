import math
a, b, v = map(int, input().split())

# 시간초과
# h = 0
# d = 1
#
# while True:
#     h += a
#     if h >= v:
#         break
#     h -= b
#     d += 1
#
# print(d)

print(math.ceil((v-a)/(a-b))+1)

#math.ceil(x)
# x보다 크거나 같은 가장 작은 정수인 x의 천장값(ceiling)을 반환합니다.
# x가 float가 아니면, x.__ceil__()에 위임하고, 이것은 Integral 값을 반환해야 합니다.

