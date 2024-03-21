# 1. 최소힙을 구하고
# 2. n개의 값을 저장
# 3. 마지막 노드부터 --> root까지 부모노드의 값을누적
# 4. 값을 출력

# 최소 힙 클래스
class MinHeap:
    def __init__(self, size):
        self.last = 0
        self.H = [0] * (size+1)  # root가 1번 인덱스부터이기 때문에

    def is_full(self):
        return self.last == len(self.H)

    def is_empty(self):
        return self.last == 0

    def insert(self, value):
        # 마지막 위치에 값을 추가
        # 완전 이진 트리이기 때문에
        self.last += 1
        self.H[self.last] = value

        # 최소 힙 조건을 만족하기 위후ㅐ
        # 자식 노드와 부모 노드의 값을 비교해서
        # 부모노드가 더 작다면 확정
        # 부모노드가 더 크다면 자식의 값과 부모의 값을 교환
        # 그리고 부모가 더 있으면 반복

