n = int(input())    #약수의 개수

div = list(map(int, input().split()))
div.sort()
num = div[0] * div[-1]

print(num)