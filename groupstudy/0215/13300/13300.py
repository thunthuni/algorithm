import sys
sys.stdin = open('input.txt')

N, k = list(map(int, input().split()))
g_cnt = [0]*6
b_cnt = [0]*6
for i in range(N):
    gender, age = list(map(int, input().split()))
    if gender == 0:
        g_cnt[age - 1] += 1
    if gender == 1:
        b_cnt[age - 1] += 1
# print(g_cnt)
# print(b_cnt)
room = 0
for i in range(6):
    if g_cnt[i] != 0:
        if g_cnt[i] % k == 0:
            room += g_cnt[i]//k
        else:
            room += g_cnt[i]//k + 1
    else:
        continue
for i in range(6):
    if b_cnt[i] != 0:
        if b_cnt[i] % k == 0:
            room += b_cnt[i] // k
        else:
            room += b_cnt[i] // k + 1
    else:
        continue
print(room)