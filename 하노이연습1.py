def TowerOfHanoi(n, s_pole, i_pole, d_pole, poles):
    if n == 1:
        # 원판 이동
        disk = poles[s_pole].pop()  # 현재 기둥에서 원판을 꺼낸다
        poles[d_pole].append(disk)  # 꺼낸 원판을 목적지 기둥에 추가한다

        # 이동 및 현재 상태 출력
        print(f"Move disc {disk} from pole {s_pole} to pole {d_pole}")
        print_poles(poles)  # 상태 출력
        return

    # 재귀 호출로 가장 작은 원판들을 이동
    TowerOfHanoi(n-1, s_pole, d_pole, i_pole, poles)

    # 가장 큰 원판 이동
    disk = poles[s_pole].pop()  # 현재 기둥에서 원판을 꺼낸다
    poles[d_pole].append(disk)  # 꺼낸 원판을 목적지 기둥에 추가한다
    print(f"Move disc {disk} from pole {s_pole} to pole {d_pole}")
    print_poles(poles)  # 상태 출력

    # 다시 재귀 호출로 원판들을 목적지로 이동
    TowerOfHanoi(n-1, i_pole, s_pole, d_pole, poles)


def print_poles(poles):
    for pole, disks in poles.items():
        print(f"{pole}: {disks}")
    print("-" * 30)

# 초기 설정
n = 3
poles = {
    'A': list(range(n, 0, -1)),  # 큰 숫자가 아래쪽 -> 내림차순 설명
    'B': [],
    'C': []
}

# 실행
print_poles(poles)
TowerOfHanoi(n, 'A', 'B', 'C', poles)


