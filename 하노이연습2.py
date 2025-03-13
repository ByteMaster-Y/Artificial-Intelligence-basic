def TowerOfHanoi(n, s_pole, i_pole, d_pole, poles, depth=0):
    indent = " " * (depth * 4)  # 들여쓰기 추가 (재귀 깊이 표시)

    print(f"{indent}Before: TowerOfHanoi({n}, {s_pole}, {i_pole}, {d_pole})")
    print_poles(poles, indent)

    if n == 1:
        disk = poles[s_pole].pop()
        poles[d_pole].append(disk)

        print(f"{indent}Move disc {disk} from pole {s_pole} to pole {d_pole}")
        print_poles(poles, indent)
        print(f"{indent}After: TowerOfHanoi({n}, {s_pole}, {i_pole}, {d_pole})\n")
        return

    TowerOfHanoi(n-1, s_pole, d_pole, i_pole, poles, depth+1)

    disk = poles[s_pole].pop()
    poles[d_pole].append(disk)

    print(f"{indent}Move disc {disk} from pole {s_pole} to pole {d_pole}")
    print_poles(poles, indent)

    TowerOfHanoi(n-1, i_pole, s_pole, d_pole, poles, depth+1)

    print(f"{indent}After: TowerOfHanoi({n}, {s_pole}, {i_pole}, {d_pole})\n")

def print_poles(poles, indent=""):
    for pole, disks in poles.items():
        print(f"{indent}{pole}: {disks}")
    print(f"{indent}" + "-" * 30)

# 초기 설정
n = 3
poles = {
    'A': list(range(n, 0, -1)),  # 큰 숫자가 아래쪽
    'B': [],
    'C': []
}

# 실행
print_poles(poles)
TowerOfHanoi(n, 'A', 'B', 'C', poles)