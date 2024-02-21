# N : 정점의 개수
# 정점이 정수-> 정점 번호와 양의 정수
    # 정점이 연산자-> 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호
# 루트 정점의 번호는 항상 1

# 왼자 -> 부모 -> 오자 순서로 탐색해야 되니까 중위순회를 사용해야 될것 같당
# 주어지는 입력값에서 왼자 오자는 필요가 없어보인다

import sys
sys.stdin = open('input.txt')

def postorder_traverse(T):# 인자는 인덱스
    if T < N + 1:
        postorder_traverse(2 * T)
        postorder_traverse(2 * T + 1)
        save.append(lst[T])

T = 10
for tc in range(1, T+1):
    N = int(input()) # 8 = 정점의 개수
    lst = [0]# 인덱스 정점번호랑 일치시키기
    save = []
    for i in range(N):
        arr = list(input().split())  # 노드 번호, 글자, 왼쪽자식, 오른쪽 자식
        lst.append(arr[1])
    # print(word_lst)
    # print(f'#{tc}', end=' ')
    postorder_traverse(1)
    print()

    stack = []
    postfix = ''
    # 연산자 우선순위 설정
    icp = {'*': 2, '/': 2, '+': 1, '-': 1}

    for i in save:
        if i in '*/+-':
            if len(stack) == 0:
                stack.append(i)
            elif len(stack) != 0:
                if icp[i] >= icp[stack[len(stack) - 1]]:
                    stack.append(i)
                elif icp[i] < icp[stack[len(stack) - 1]]:
                    # 빈 리스트는 암시적 판단으로 False로 판단된다.
                    # 스택이 비어있다면 단축평가로 인해 뒤쪽 조건을 확인하지 않는다.
                    while stack and icp[i] <= icp[stack[len(stack) - 1]]:
                        # 반복문과 pop 을 같이 사용할 때 인덱스 에러가 날 수 있다. 그러므로 조건문을 잘 설정해야 한다.
                        a = stack.pop()
                        postfix += a
                    stack.append(i)
        else:
            postfix += i
    while len(stack) != 0:  # 그냥 len(stack) 도 가능
        postfix += stack.pop()

    num_stack = []
    for j in postfix:
        if j not in '+*/-':
            num_stack.append(int(j))
        elif j == '+':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a + b)
        elif j == '*':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a * b)
        elif j == '/':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a / b)
        elif j == '-':
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(a - b)
    print(f'#{tc} {num_stack.pop()}')