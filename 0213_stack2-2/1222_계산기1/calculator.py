import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    num = str(input())

    top = -1
    stack = [0] * 100
    postfix = ''

    for i in num:
        if top == -1 and i == '+': # 탑이 비어있고 연산자인경우
            top += 1  # 푸쉬
            stack[top] = i
        elif top != -1 and i == '+':
            top -= 1
            postfix += i
            top += 1
            stack[top] = i
        elif i != '+':
            postfix += i
    while top >= 0:
        top -= 1
        postfix += stack[top + 1]

    num_stack = [0] * 100
    for j in postfix:
        if j != '+':
            top += 1
            num_stack[top] = int(j)
        else:
            top -= 2
            a = num_stack[top + 1]
            b = num_stack[top + 2]
            top += 1
            num_stack[top] = a + b

    print(f'#{tc} {num_stack[top]}')



    # sum_v = 0
    # for integ in range(0, len(postfix), 2):
    #     sum_v += int(num[integ])
    #
    # print(sum_v)




