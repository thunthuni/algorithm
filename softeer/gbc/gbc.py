import sys
sys.stdin = open('input.txt')

# d = [0]
# s = []

arr = [0]*101

N, M = list(map(int, input().split()))
a = 1
for i in range(N):
    distance, speed = list(map(int, input().split()))
    for j in range(a, a+distance):
        arr[j] = speed
    a += distance

calc = 0
max_v = 0
a = 1
for i in range(M):
    distance, speed = list(map(int, input().split()))
    # 내가 체크해야할 구간이 N의 거리 내
    for j in range(a, a+distance):
        calc = speed - arr[j]
        if max_v < calc:
            max_v = calc
print(max_v)

    # rd.append(distance+rd[i])
    # rs.append(speed)


# print(d)
# print(s)
