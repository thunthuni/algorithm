# bfs 코드 작성해서 정태완에게 보낼것
# 참고 자료 없이
import sys
sys.stdin = open('input.txt')


def bfs(start_node):
    N, M = list(map(int, input().split()))  # 노드, 선 개수
    arr = list(map(int, input().split()))  # 리스트 가져오기
    adjl = [[] for _ in range(N+1)]  # 인접배열
    for i in range(N+1):
        num1, num2 = arr[i*2], arr[i*2+1]  # 이건....음...흐음아
        adjl[num1].append(num2)
        adjl[num2].append(num1)

    q = []
    sequence = []  # 노드를 방문한 순서
    visited = [-1] * (N + 1)  # -1 f

    q.append(start_node)  # 아아아아ㅏ 시작점 생성? 하기
    visited[start_node] = 0  # 방문기록 해주고

    while q: # 큐에 남은게 없을 때까지
        t = q.pop(0)
        sequence.append(t)
        for i in adjl[t]:
            if visited[i] == -1: # 방문하지 않았다면
                q.append(i)
                visited[i] = 1 + visited[t]
    return sequence


print(f'#1', *bfs(1))
