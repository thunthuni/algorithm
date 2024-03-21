# 9시부터 18시까지 가능
# 두 회의 시간이 1시간 이상 겹치면 안됨
# 구하고자 하는 것: 회의실별로 비어 있는 시간대
# 9 이상 18이하
# 출력값: 회의실 이름의 오름차순

names = []
N, M = list(map(int, input().split()))
for tc in range(N):
    a = input()
    names.append(a)
# 딕셔너리로 만들고 싶당 
    
reserve = [[]*N]
for tc in range(M):
    room, start, end = list(map(str, input().split()))
    i = names.index(room)
    reserve[i].append(tuple(start, end))

count = [0]*10
hours = list(range(9, 19))
# reserve.sort(key=lambda x: (x[1], x[0])