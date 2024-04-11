# 1: 스위치 켜져 있음 / 0: 꺼져있음
# 자신의 성별/ 받은 수에 따라서 스위치 조작 방식이 다름
    # 남: 스위치 번호의 배수번호에 해당하는 스위치의 상태를 뒤집음
    # 여: 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
        #  가장 많은 스위치를 포함하는 구간을 찾아서
        #  그 구간에 속한 스위치의 상태를 모두 바꾼다

import sys
sys.stdin = open('input.txt')
def change(lst):
    for i in range(len(lst)):
    # 스위치 뒤집는 함수 생성

N = int(input())  # 스위치의 개수
switches = list(map(int, input().split()))
N_stu = int(input())
for _ in range(N_stu):
    gender, num = list(map(int, input().split()))
    if gender == 1:  # 학생이 남학생이라면
        for i in range(1, N):
            if switches[num*i] == 1:
                switches[num*i] = 0
            else:
                switches[num*i] = 1
    else:  # 여학생이라면
