import sys
sys.stdin = open('input.txt')

switch_num = int(input())
switches = list(map(int, input().split()))
student_num = int(input())
lst = [3]
for v in switches:
    lst.append(v)

for _ in range(student_num):
    gender, N = list(map(int, input().split()))

    for i in range(switch_num):
        if gender == 1:
            if i > 0:
                if i % N == 0:
                    if lst[i] == 0:
                        lst[i] = 1
                    elif lst[i] == 1:
                        lst[i] = 0
                else:
                    continue
        elif gender == 2:
            j = 1
            while N + j < switch_num and N-j >= 0:
                if lst[j + N] == lst[N - j]:
                    j += 1
                    continue
                else:
                    break

            for idx in range(j):
                if lst[N]
                if lst[N + idx] == 0:
                    lst[N + idx] = 1
                elif lst[N + idx] == 1:
                    lst[N + idx] = 0
                if lst[N - idx] == 0:
                    lst[N - idx] = 1
                elif lst[N - idx] == 1:
                    lst[N - idx] = 0

print(lst[1:switch_num+1])