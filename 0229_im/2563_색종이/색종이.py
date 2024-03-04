import sys
sys.stdin = open('input.txt')

arr = [[0]*100 for _ in range(100)]
N = int(input())  # 색종이의 수
for tc in range(N):
    L, D = list(map(int, input().split()))
    # L : 도화지 왼쪽 변 -> 색종이 왼쪽 변
    # D : 도화지 아래쪽 변 -> 색종이 아래쪽 변
    # 색종이는 10*10 으로 일정한 크기이다
    # (L,D) 는 색종이의 왼쪽 아래 꼭짓점 좌표라고 할 수 있다
    # L: row D: col

    for row in range(L, L+10):
        for col in range(D, D+10):
            arr[row][col] = 1

sum_v = 0
for row in range(100):
    sum_v += arr[row].count(1)
print(sum_v)