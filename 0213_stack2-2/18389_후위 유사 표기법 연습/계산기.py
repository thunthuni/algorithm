import sys
sys.stdin = open('input.txt')

T = (int(input()))
for tc in range(1, T+1):
    function = str(input())

    # 내가 필요한 조건
    # 1. 피연산자 숫자라면 ! 바로 출력
    # 2. 연산자 +,*,/,- 라면 우선순위가 top 보다 크거나 같으면 push
        # 작으면 문자보다 작은게 나올 때까지 pop
    # 3. 더이상 읽을게 없으면 이미 출력된 피연산자들 + 스택에 남아있는 연산자들 해서 출력

    top = -1
    stack = [0] * 100
    icp = {'*': 2, '/': 2, '+': 1, '-': 1}
    isp = {'*': 2, '/': 2, '+': 1, '-': 1}
    postfix = ''

    for i in function:
        if i in '*/+-':      # 문자가 숫자가 아니라 연산자라면
            if top == -1:      # 스택이 비어있다면
                top += 1
                stack[top] = i  # 바로 푸쉬
            elif top != -1:    # 스택이 비어있지 않다면
                if isp[stack[top]] <= icp[i]: # 만약 top 에 있는 연산자가 우선순위가 들어가는 애 보다 우선순위가 낮거나 같다면
                    top += 1
                    stack[top] = i
                elif isp[stack[top]] > icp[i]:  # 만약 우선순위가 크다면
                    while isp[stack[top]] > icp[i]:
                        top -= 1
                        postfix += stack[top+1]
                    top += 1
                    stack[top] = i
        else:
            postfix += i
    while top >= 0:
        top -= 1
        postfix += stack[top+1]

    print(f'#{tc} {postfix}')




