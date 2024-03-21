def dfs(i, V):  # 시작 i, 마지막 V
    visited = [0] * (V + 1)  # visited, stack 생성 및 초기화
    st = []
    visited[i] = 1  # 시작점 방문
    print(f'#1 {i}', end='')
    while True:  # 탐색시작
        for w in adjl[i]:  # 현재 방문한 정점에 인점하고 방문안한 정점 w가 있으면
            if visited[w] == 0:
                st.append(i)  # push(i), i 를 지나서
                i = w  # w에 방문
                visited[i] = 1  # 방문해서 할일
                print(f'-{i}', end='')
                break
        else:  # i에 남은 인접 정점이 없으면
            if st:  # 스택이 비어있지 않으면
                i = st.pop()
            else:
                break


t, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접리스트를 생성하자
adjl = [[] for _ in range(100)]  # adjl[i] 행에 i에 인접인 정점번호를 저장
for i in range(len(arr)):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)  # 무향그래프 라는 것이지

print(adjl)
# dfs(1, V)