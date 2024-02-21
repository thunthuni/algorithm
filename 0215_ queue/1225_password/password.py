import sys
sys.stdin = open('input.txt')

def isempty():
    return front == rear

def isfull():
    return(rear+1) % len(q) == front

def dequeue():
    global front
    if isempty():
        print('Queue_Empty')
    else:
        front = (front + 1) % len(q)
        return q[front]


T = int(input())
for tc in range(1, T+1):
    q = list(map(int, input().split()))

    # 초기 공백 큐생성
    N = len(q)
    front = rear = 0

# (front + 1) 이 rear로 이동