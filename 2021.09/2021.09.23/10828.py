# 한 쪽 끝에서만 자료를 넣고 뺄 수 있는 LIFO(Last In First Out)형식의 자료 구조
# 스택(Stack0는 LIFO를 따름
# 가장 최근에 스택에 추가한 항목이 가장 먼저 제거될 항목
# pop(): 스택에서 가장 위에 있는 항목을 제거
# push(item): item 하나를 스택의 가장 윗 부분에 추가
# peek(): 스택의 가장 위에 있는 항목을 반환
# isEmpty(): 스택이 비어 있을 때에 true를 반환
# https://gmlwjd9405.github.io/2018/08/03/data-structure-stack.html

n = int(input())
li = []

# push일 때만 숫자를 입력 받는 건 어떻게 해야할지?
for _ in range(n):
