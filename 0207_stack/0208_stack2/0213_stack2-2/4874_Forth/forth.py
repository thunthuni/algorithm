import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    my_str = input().split()

    # 일단 먼저 스택에 숫자를 넣어주자
    # 그 다음에 연산자를 만나면 계산을 해주고

    top = -1
    num_stack = [0] * 100
    for j in my_str:
        if j not in '+/*-.':  # 피연산자가 숫자일 때
            top += 1
            num_stack[top] = int(j)

        else:       # 연산자일 때
            if j == '.':
                break

            top -= 2
            a = num_stack[top + 1]
            b = num_stack[top + 2]
            calc_dict = {
                '+' : a+b, '-': a-b, '*': a*b, '/': a//b
            }
            top += 1
            num_stack[top] = calc_dict[j]
    if top != 0:
        print(f'#{tc} error')
    else:
        print(f'#{tc} {num_stack[top]}')

