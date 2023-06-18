# https://contest.yandex.ru/contest/27663/problems/B/

def get_intersection_of_sets(numbers_string_1: str, numbers_string_2: str) -> set[int]:
    set_1, set_2 = set(map(int, numbers_string_1.split())), \
        set(map(int, numbers_string_2.split()))
    result = set()
    for number in set_1:
        if number in set_2:
            result.add(number)
    return result


def main():
    numbers_string_1, numbers_string_2 = input(), input()
    print(*get_intersection_of_sets(numbers_string_1, numbers_string_2))


if __name__ == '__main__':
    main()
