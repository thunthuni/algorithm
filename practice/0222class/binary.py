N = map(int, input().split())
M = len(N)
for i in range(M, -1, 4):
    if N[i:M-4] in