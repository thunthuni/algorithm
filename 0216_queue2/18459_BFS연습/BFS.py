import sys
sys.stdin = open('input.txt')

def bfs(s, N):
    q = []
    visited = [0] * (N+1)
    q.append(s)
    visited[s] = 1
    lst = []
    while q:
        t = q.pop(0)
        lst.append(t)
        for i in adjl[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1 + visited[t]
    print(f'#1 {lst}')

V, E = map(int, input().split())
arr = list(map(int, input().split()))
adjl = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = arr[i*2], arr[i*2+1]
    adjl[n1].append(n2)
    adjl[n2].append(n1)
# print(adjl)
bfs(1, V)

