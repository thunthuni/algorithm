# 9시부터 18시까지 가능
# 두 회의 시간이 1시간 이상 겹치면 안됨
# 구하고자 하는 것: 회의실별로 비어 있는 시간대
# 9 이상 18이하
# 출력값: 회의실 이름의 오름차순

name_lst =[]
N, M = list(map(int, input().split()))
for tc in range(N):
    a = input()
    name_lst.append(a)

rooms = [[]*N for _ in range(N)]
for tc in range(M):
    room, start, end = list(map(str, input().split()))
    i = name_lst.index(room)
    rooms[i].append((start, end))

count = [0] * 10
hours = list(range(9, 19))

for idx in range(N):
    for i in range(len(rooms[idx])):
        for j in range(int(rooms[idx][i][0]), int(rooms[idx][i][1])):
            if j in list(range(int(rooms[idx][i+1][0]), int(rooms[idx][i][1]))):
                continue
            else:


    # hrs_lst = []
    # for index in range(len(hours)):
    #     if index + 1 < len(hours):
    #         if hours[index] + 1 == hours[index+1]:
    #             hrs_lst.append(hours[index])
    #         else:





# print(rooms)
print(hours)