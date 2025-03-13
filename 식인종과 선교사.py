#너비 우선 탐색(BFS) 알고리즘을 사용하여 상태를 탐색
from collections import deque

# 상태를 나타내는 클래스
class State:
    def __init__(self, missionaries_left, cannibals_left, boat_position, missionaries_right, cannibals_right):
        self.missionaries_left = missionaries_left  # 왼쪽에 있는 선교사 수
        self.cannibals_left = cannibals_left  # 왼쪽에 있는 식인종 수
        self.boat_position = boat_position  # 배의 위치 (0: 왼쪽, 1: 오른쪽)
        self.missionaries_right = missionaries_right  # 오른쪽에 있는 선교사 수
        self.cannibals_right = cannibals_right  # 오른쪽에 있는 식인종 수
        self.parent = None  # 이전 상태를 추적하기 위한 부모 상태

    # 상태가 유효한지 확인하는 함수
    def is_valid(self):
        if self.missionaries_left < 0 or self.cannibals_left < 0 or self.missionaries_right < 0 or self.cannibals_right < 0:
            return False
        if (self.missionaries_left > 0 and self.missionaries_left < self.cannibals_left) or (self.missionaries_right > 0 and self.missionaries_right < self.cannibals_right):
            return False
        return True

    def __str__(self):
        return f"({self.missionaries_left}, {self.cannibals_left}) -> ({self.missionaries_right}, {self.cannibals_right}), Boat: {'Left' if self.boat_position == 0 else 'Right'}"

# BFS를 이용한 탐색
def bfs():
    start = State(3, 3, 0, 0, 0)  # 초기 상태
    goal = State(0, 0, 1, 3, 3)  # 목표 상태
    queue = deque([start])  # 큐에 시작 상태를 넣음
    visited = set()  # 방문한 상태들을 저장
    visited.add((start.missionaries_left, start.cannibals_left, start.boat_position))

    while queue:
        current_state = queue.popleft()

        # 목표 상태에 도달하면 경로 출력
        if current_state.missionaries_left == goal.missionaries_left and current_state.cannibals_left == goal.cannibals_left:
            path = []
            while current_state:
                path.append(current_state)
                current_state = current_state.parent
            path.reverse()
            for state in path:
                print(state)
            return

        # 가능한 새로운 상태를 계산하여 큐에 추가
        possible_moves = get_possible_moves(current_state)
        for move in possible_moves:
            if (move.missionaries_left, move.cannibals_left, move.boat_position) not in visited and move.is_valid():
                visited.add((move.missionaries_left, move.cannibals_left, move.boat_position))
                move.parent = current_state  # 부모 상태를 기록
                queue.append(move)

# 가능한 이동을 계산하는 함수
def get_possible_moves(state):
    moves = []
    if state.boat_position == 0:  # 배가 왼쪽에 있을 때
        moves.append(State(state.missionaries_left - 1, state.cannibals_left - 1, 1, state.missionaries_right + 1, state.cannibals_right + 1))  # 1명 선교사, 1명 식인종
        moves.append(State(state.missionaries_left - 2, state.cannibals_left, 1, state.missionaries_right + 2, state.cannibals_right))  # 2명 선교사
        moves.append(State(state.missionaries_left, state.cannibals_left - 2, 1, state.missionaries_right, state.cannibals_right + 2))  # 2명 식인종
        moves.append(State(state.missionaries_left - 1, state.cannibals_left, 1, state.missionaries_right + 1, state.cannibals_right))  # 1명 선교사
        moves.append(State(state.missionaries_left, state.cannibals_left - 1, 1, state.missionaries_right, state.cannibals_right + 1))  # 1명 식인종
    else:  # 배가 오른쪽에 있을 때
        moves.append(State(state.missionaries_left + 1, state.cannibals_left + 1, 0, state.missionaries_right - 1, state.cannibals_right - 1))  # 1명 선교사, 1명 식인종
        moves.append(State(state.missionaries_left + 2, state.cannibals_left, 0, state.missionaries_right - 2, state.cannibals_right))  # 2명 선교사
        moves.append(State(state.missionaries_left, state.cannibals_left + 2, 0, state.missionaries_right, state.cannibals_right - 2))  # 2명 식인종
        moves.append(State(state.missionaries_left + 1, state.cannibals_left, 0, state.missionaries_right - 1, state.cannibals_right))  # 1명 선교사
        moves.append(State(state.missionaries_left, state.cannibals_left + 1, 0, state.missionaries_right, state.cannibals_right - 1))  # 1명 식인종

    return moves

# BFS 실행
bfs()
