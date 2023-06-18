# https://contest.yandex.ru/contest/27663/problems/H/


def get_minimal_shots_count(birds_coordinates: list[tuple[int]]) -> int:
    unique_x_coordinates = set()
    for bird in birds_coordinates:
        unique_x_coordinates.add(bird[0])
    return len(unique_x_coordinates)


def main():
    birds_count = int(input())
    birds_coordinates = []
    for _ in range(birds_count):
        birds_coordinates.append(tuple(map(int, input().split())))
    result = get_minimal_shots_count(birds_coordinates)
    print(result)


if __name__ == '__main__':
    main()
