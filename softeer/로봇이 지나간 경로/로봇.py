import sys
sys.stdin = open('input.txt')

# H행 W열의 2차원 격자판 위를 돌아다니는 로봇쿤
# 이동을 제어하는 명령어
    # L: 왼쪽으로 90도 턴 방향 바뀜
    # R: 오른쪽으로 90도 턴 방향 바뀜
    # A: 바라보는 방향을 두칸 전진
        # if not 0 <= nr < H and 0 <= nc < w: 명령 수행 안됨

# 구하고자 하는 것
    # 1. 처음에 로봇을 두어야 하는 칸의 좌표/ 어떤 방향으로 두어야 하는가?
    # 2. 이후에 로봇에게 입력할 명령어의 순서
    # 단, 명령어의 개수를 최소화 할것


# 한 번 이상의 A명령을 내렸다 => 방문한 칸수가 최소 3개 이상
# 같은 칸을 두번 이상 방문 X
# '#': 방문 '.': 방문 X

H, W = list(map(int, input().split()))
arr = [list(input()) for _ in range(H)]

# 어떻게 풀면 좋을까??
# 일단 길을 가는것만 하는게 아니라 명령어를 '최소'로 사용해야되기 때문에
# 완전탐색을 사용해야 할 듯 하다. => BFS? or DFS?
# 시작점을 어떻게 찾으면 좋을까
    # 말그대로 '#' 이 처음 시작하는 지점이니까
    # 좌표중에서 세방향은 '.'이고 한방향만 '#'곳을 찾으면 되지 않을까..?
# 시작점을 찾은 후에 # 을 따라 이동할건데
    # 명령어의 타입과 횟수를 저장하면서 가야한다

dr = [-1, 0, -1, 0] # 상우하좌
dc = [0, 1, 0, -1]
start = []

for r in range(H):
    for c in range(W):
        cnt = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < H and 0 <= nc < W and arr[nr][nc] == '#':
                cnt += 1
                if cnt > 1:
                    break
        if cnt == 1:
            start.append((nr, nc))
print(start)