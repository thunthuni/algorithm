import sys
sys.stdin = open('input.txt')


def inorder_traverse(T):# 인자는 인덱스
    if T < N + 1:
        inorder_traverse(2*T)
        print(word_lst[T], end='')
        inorder_traverse(2*T + 1)


T = 10
for tc in range(1, T+1):
    N = int(input()) # 8 = 정점의 개수
    word_lst = [0] # 인덱스 정점번호랑 일치시키기
    for i in range(N):
        arr = list(input().split())  # 노드 번호, 글자, 왼쪽자식, 오른쪽 자식
        word_lst.append(arr[1])
    # print(word_lst)
    print(f'#{tc}', end=' ')
    inorder_traverse(1)
    print()

# 주석 달기
# 흐름 잡기 위해서
# 문제에서 정보 최대한 얻기