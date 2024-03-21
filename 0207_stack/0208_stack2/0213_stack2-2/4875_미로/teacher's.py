# 모든 길 탐색했을 때 찾으면 3/ 없으면 1
# 재귀, stack  : 돌아올 경로 저장
# 벽을 만났을 때 가지치기
import sys
sys.stdin = open('input.txt')

class Stack:
    def __init__(self, size):
        self.top = -1
        self.stack = [0] * size
    def peek(self):
        return self.stack[self.top]

    def is_full(self):
        # top 이 마지막 인덱스에 위치해 있는지 비교
        return self.top == len(self.stack) - 1

    def push(self, value):
        if self.is_full():
            print('Full~~~~~')
            return 0
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.is_empty():
            print('Empty~~')
            return 0
        else:
            value = self.peek()
            self.stack[self.top]

T = int(input())
for tc in range(1, T+1):
    pass