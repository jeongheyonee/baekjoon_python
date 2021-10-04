# 나는 국어를 못하나봐,,,, 문제가 이해가 안되는 걸~ 고민을 더 해봐야겠다!
# https://assaeunji.github.io/python/2020-05-04-bj1966/
# https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%801966%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%ED%94%84%EB%A6%B0%ED%84%B0-%ED%81%90

testCase = int(input())

for _ in range(testCase):
    N, M = map(int, input().split())

    printList = list(map(int, input().split()))
    checkList = [0 for _ in range(N)]
    checkList[M] = 1  # 궁금한 문서위치 저장

    count = 0
    while True:
        if printList[0] == max(printList):
            count += 1

            if checkList[0] != 1:
                del printList[0]
                del checkList[0]
            else:
                print(count)
                break
        else:
            printList.append(printList[0])
            checkList.append(checkList[0])
            del printList[0]
            del checkList[0]
