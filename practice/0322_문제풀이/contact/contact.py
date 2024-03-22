# 1. 자료구조:
# - 그래프(인접행렬, 인접리스트)
# 2. 알고리즘
# - BFS
    # 라는 생각이 들었으면 검증이 필요하다
    # BSF 알고리즘은 맞고 추가동작이 필요함

    # 인접배열 안에 남은 노드가 없을 때까지 BFS 함수를 돌리는데
    # 레벨별로 노드를 출력해서 묶어주고 마지막 레벨에 있는 노드를 출력하면 될듯?
# BFS의 시간복잡도
# 계산 방법: 얼마나 방문 할 수 있나?
# 노드의 수가 최대 100개
# 간선의 수 => 0(V+E) (인접 리스트 기준)
# => 완전탐색 가능하겠다~~

import sys
sys.stdin = open('input.txt','r')


def bfs(start):
    q = [start]
    visited = [0]*101
    visited[start] = 1

    # 가장 깊은 depth의 가장 큰 수
    max_number = start
    # 가장 깊은 depth를 저장
    max_depth = 1

    while q:
        now = q.pop()
        # 갈 수 있는 곳들
        for to in graph[now]:
            # 이미 방문했다면 pass
            if visited[to]:
                continue

            # 현재 방문 = 이전방문 + 1번만에 왔다는 의미
            visited[to] = visited[now] + 1

            # depth 가 더 깊어지면 => max_number초기화
            # depth 는 같은데 숫자가 더 큼 => 초기화
            if max_depth < visited[to] or (max_depth == visited[to] and max_number < to):
                max_depth = visited[to]
                max_number = to
            # or q.append((to,depth))
            q.append(to)
    return max_number

T = 10
for tc in range(1, 11):
    N, start = map(int, input().split())  # 노드의 수, 시작 노드
    input_graph = list(map(int, input().split()))
    # 인접 리스트
    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        s = input_graph[i]
        e = input_graph[i+1]
        graph[s].append(e)

    r = bfs(start)
    print(r)