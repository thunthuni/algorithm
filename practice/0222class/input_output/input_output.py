import sys
sys.stdin = open('input.txt', 'r')
sys.stout = open('output.txt', 'w')

a, b = map(int, input().split())

print(a * b)

