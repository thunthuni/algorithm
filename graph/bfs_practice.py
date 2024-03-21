import sys
sys.stdin = open('input.txt')

def bfs(s):
    q = [] #  큐
    q.append(s)  # 큐에 시작점 넣기
    visited[s] = 1  # 방문 처리
    lst = []  # 경로 저장할 리스트
    while q:
        t = q.pop()
        lst.append(t)
        for i in adjl[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1
    print(lst)

V, E = map(int, input().split())
arr = list(map(int, input().split()))
visited = [0]*E
# 인접 배열 만들기
adjl = [[] for _ in range(E)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    # 양방향 그래프
    adjl[n1].append(n2)
    adjl[n2].append(n1)

bfs(1)
