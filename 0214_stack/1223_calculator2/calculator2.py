import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    num = input()

    stack = []
    postfix = ''

    # 후위 표기식으로 바꿔보자
    # 안밖 우선순위 설정해주자
    icp = {'*': 2, '+': 1}
    isp = {'*': 2, '+': 1}
    # 문자가 들어오는데 피연산자이면 출력
        # 연산자이면
            # 스택이 비어있을 때는 스택에 푸쉬
            # 스택이 비어있지 않을 때는
                    # 안 priority < 밖 priority : push
                    # 안 priority >= 밖 priority: 안에 있는거 pop 하고 들어가
    # 마지막으로 스택이 -1 이 될 때까지 다 출력해서 postfix에 더해줘!

    for i in num:
        if i in '*+':
            if len(stack) == 0:
                stack.append(i)
            elif len(stack) != 0:
                if icp[i] > isp[stack[len(stack)-1]]:
                    stack.append(i)
                elif icp[i] <= isp[stack[len(stack)-1]]:
                    # 빈 리스트는 암시적 판단으로 False로 판단된다.
                    # 스택이 비어있다면 단축평가로 인해 뒤쪽 조건을 확인하지 않는다.
                    while stack and icp[i] <= isp[stack[len(stack)-1]]:
                    # 반복문과 pop 을 같이 사용할 때 인덱스 에러가 날 수 있다. 그러므로 조건문을 잘 설정해야 한다.
                        a = stack.pop()
                        postfix += a
                    stack.append(i)
        else:
            postfix += i
    while len(stack) != 0: # 그냥 len(stack) 도 가능
        postfix += stack.pop()


# numberstack 을 만들어줘!
    num_stack = []
    for j in postfix:
        if j not in '+*':
            num_stack.append(int(j))
        elif j == '+':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a + b)
        elif j == '*':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a*b)
    print(f'#{tc} {num_stack.pop()}')