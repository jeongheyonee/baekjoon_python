import math

x, y, w, h = map(int, input().split())
print(min(x, y, abs(w-x), abs(h-y)))

# d = []
# d.append(math.sqrt(x**2 + y**2))
# d.append(math.sqrt((w-x)**2 + (h-y)**2))
# d.append(math.sqrt(x**2 + (h-y)**2))
# d.append(math.sqrt((w-x)**2 + y**2))
# d.append(abs(w-x))
# d.append(abs(x-w))
# d.append(abs(h-y))
# d.append(abs(y-h))
#
# print(min(d))
# 틀린 코드 -> 대각선의 경우는 계산하지 않음!
# 경계선에 도달해야 하므로 꼭짓점까지의 경우는 생각하지 않음