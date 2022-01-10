# 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO(Last In First Out)형식의 자료 구조
# 스택(Stack0는 LIFO를 따름
# 가장 최근에 스택에 추가한 항목이 가장 먼저 제거될 항목
# pop(): 스택에서 가장 위에 있는 항목을 제거
# push(item): item 하나를 스택의 가장 윗 부분에 추가
# peek(): 스택의 가장 위에 있는 항목을 반환
# isEmpty(): 스택이 비어 있을 때에 true를 반환
# https://gmlwjd9405.github.io/2018/08/03/data-structure-stack.html
import sys

input = sys.stdin.readline

n = int(input())
stack = []

# push일 때만 숫자를 입력 받는 건 어떻게 해야할지?
for _ in range(n):
    word = input().split()
    order = word[0]

    if order == 'push':
        value = word[1]
        stack.append(value)

    elif order == 'pop':
        if len(stack)== 0:
            print(-1)
        else:
            print(stack.pop())

    elif order == 'size':
        print(len(stack))

    elif order == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif order == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])