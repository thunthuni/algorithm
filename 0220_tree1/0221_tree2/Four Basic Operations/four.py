# N : 정점의 개수
# 정점이 정수-> 정점 번호와 양의 정수
    # 정점이 연산자-> 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호
# 루트 정점의 번호는 항상 1

# 왼자 -> 부모 -> 오자 순서로 탐색해야 되니까 중위순회를 사용해야 될것 같당
# 주어지는 입력값에서 왼자 오자는 필요가 없어보인다

import sys
sys.stdin = open('input.txt')

# def postorder_traverse(T):# 인자는 인덱스
#     if T < N + 1:
#         postorder_traverse(2 * T)
#         postorder_traverse(2 * T + 1)
#         save.append(lst[T])

T = 10
for tc in range(1, T+1):
    N = int(input()) # 8 = 정점의 개수
    lst = [0]# 인덱스 정점번호랑 일치시키기
    left = [0] * (N+1)
    right = [0] * (N+1)
    par = [0] * (N+1)

    for i in range(N):
        arr = list(input().split())  # 노드 번호, 노드값, 왼쪽자식, 오른쪽 자식
        # for j in range(N+1):
            p, c = arr[0], arr[i * 2 + 1]
            if left[p] == 0:
                left[p] = c
            else:
                right[p] = c
            par[c] = p

    print(left)
    print(right)
    # postorder_traverse(1)
    # print()
    # print(save)

    # num_stack = []
    # for j in save:
    #     if j not in '+*/-':
    #         num_stack.append(int(j))
    #     elif j == '+':
    #         a = num_stack.pop()
    #         b = num_stack.pop()
    #         num_stack.append(a + b)
    #     elif j == '*':
    #         a = num_stack.pop()
    #         b = num_stack.pop()
    #         num_stack.append(a * b)
    #     elif j == '/':
    #         a = num_stack.pop()
    #         b = num_stack.pop()
    #         num_stack.append(b // a)
    #     elif j == '-':
    #         a = num_stack.pop()
    #         b = num_stack.pop()
    #         num_stack.append(b - a)
    # print(f'#{tc} {num_stack.pop()}')
