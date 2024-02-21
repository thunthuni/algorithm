import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    brackets = input()

    stack = []
    for idx in range(len(brackets)):
        if brackets[idx] == '(':
            stack.append('(')
        if brackets[idx] == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                print(-1)
                break
    else: # 조건은 반복문이 정상적으로 작동했을 때 (break일 때 실행안됨)
        if len(stack) == 0:
            print(1)
        else:
            print(-1)




