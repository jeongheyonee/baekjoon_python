def hansu(n):
    cnt = 0
    for i in range(1, n+1):
        n_list = list(map(int, str(i)))
        #str(n): 숫자를 문자열로 만들어 줌
        #map(int, str(n)): 문자열로 되어있는 각 자릿수를 정수로 바꾸어줌줌
        if i < 100:
            cnt += 1
        else:
            if n_list[1] - n_list[0] == n_list[2] - n_list[1]:
                cnt += 1
    return cnt

n = int(input())
print(hansu(n))