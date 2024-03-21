import sys
sys.stdin = open('input.txt')

result = []
def dfs(i):  # 시작 i, 마지막 V
    global result
    if result == 1:
        return
    visited[i] = 1  # 시작점 방문
    # result.append(i)
    if i != 99:
        for w in adjl[i]:
            if visited[w] == 0:
                dfs(w)
    else:
        result = 1

T = 10
for tc in range(1, T+1):
    t, E = map(int, input().split())
    arr = list(map(int, input().split()))
    result = 0
    # 인접리스트를 생성하자
    adjl = [[] for _ in range(100)]  # adjl[i] 행에 i에 인접인 정점번호를 저장
    for i in range(E):
        n1, n2 = arr[i * 2], arr[i * 2 + 1]
        adjl[n1].append(n2)
        # adjl[n2].append(n1)  # 무향그래프 라는 것이지
          # visited, stack 생성 및 초기화

    visited = [0] * 100
    dfs(0)
    print(f'#{tc} {result}')



