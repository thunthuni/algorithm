import sys
sys.stdin = open('input.txt')

# 우선순위큐를 활용
from heapq import heappush, heappop


def prim(start):
    pq = []
    MST = [0] * V
    # 최소 비용
    sum_weight = 0

    # 시작점 추가
    # [기존] 노드 번호만 관리
    # [prim] 가중치가 낮으면 먼저 나와야 한다.
    #  -> 관리해야할 데이터: 가중치, 노드 번호 2가지
    # -> 동시에 두가지 데이터 다루기
    #          1. class로 만들기
    #          2. tuple로 관리
    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)
        print(now, '/', MST)
        # 방문처리
        MST[now] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈 수 잇는 노드들을 보면서
        for to in range(V):
            # 갈 수 없거나 이미 방문햇다면 pass
            if graph[now][to] == 0 or MST[to]:
                continue

            heappush(pq, (graph[now][to], to))
    print(f'최소비용: ')
V, E = map(int, input().split())
# 인접 리스트로 저장
graph = [[0] * V for _ in range(V)]
for _ in range(E):
    s,e,w = map(int, input().split())
    # 가중치 저장
    # 기존 3 -> 4로 갈 수 있다
    # graph[3][4] = 1
    # 가중치 그래프: 3 -> 4로 가는데 31 이라는 비용이 든다
    # graph[3][4] = 31
    graph[s][e] = w
    graph[e][s] = w  # 무방향 그래프

print(graph)

