# 패턴 찾기 문제
import sys
sys.stdin = open('input.txt')

M, N, K = list(map(int, input().split()))
method = input()
buttons = input()

if method in buttons:
    print('secret')
else:
    print('normal')