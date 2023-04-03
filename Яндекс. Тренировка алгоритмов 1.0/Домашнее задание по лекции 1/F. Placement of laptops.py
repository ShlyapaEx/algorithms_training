# https://contest.yandex.ru/contest/27393/problems/F

def main():
    a1, b1, a2, b2 = map(int, input().split())
    solutions = {}

    side10 = a1 + a2
    side20 = max(b1, b2)
    area1 = side10 * side20
    solutions[area1] = (side10, side20)

    side21 = a1 + b2
    side22 = max(b1, a2)
    area2 = side21 * side22
    solutions[area2] = (side21, side22)

    side31 = b1 + a2
    side32 = max(a1, b2)
    area3 = side31 * side32
    solutions[area3] = (side31, side32)

    side41 = b1 + b2
    side42 = max(a1, a2)
    area4 = side41 * side42
    solutions[area4] = (side41, side42)

    min_area = min(solutions.keys())
    return solutions[min_area]


if __name__ == '__main__':
    print(*main())
