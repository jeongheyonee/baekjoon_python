N, K = map(int, input().split())
csum = 0
A = []
for _ in range(N):
    A.append(int(input()))
A = sorted(A, reverse = True) # 배열 A를 큰 수부터 내림차순으로 정렬
for i in range(N):
    ccount = K//A[i]
    csum += ccount
    K -= (ccount)*A[i]
    if K == 0: # 나머지 금액이 0인 경우 반복문 탈출
        break
print(csum)

# https://it-college-diary.tistory.com/entry/%EA%B7%B8%EB%A6%AC%EB%94%94-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-11047%EB%B2%88-%EB%8F%99%EC%A0%840
