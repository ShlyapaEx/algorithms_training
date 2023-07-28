# https://contest.yandex.ru/contest/27794/problems/D/


def get_possible_combinations_count(min_range: int, numbers: tuple[int]) -> int:
    combinations_count = 0
    end = 1
    for start in range(len(numbers) - 1):
        while end < len(numbers) \
                and abs(numbers[start] - numbers[end]) <= min_range:
            end += 1
        combinations_count += len(numbers) - end
    return combinations_count


def main():
    statues_count, min_range = map(int, input().split())
    numbers = tuple(map(int, input().split()))

    result = get_possible_combinations_count(min_range, numbers)
    print(result)


if __name__ == '__main__':
    main()
