# https://contest.yandex.ru/contest/27794/problems/B/


def create_prefix_sums(numbers: tuple) -> list[int]:
    prefix_sums = [0] * (len(numbers) + 1)

    for i in range(1, len(numbers) + 1):
        prefix_sums[i] += prefix_sums[i - 1] + numbers[i - 1]

    return prefix_sums


def get_number_pairs_count(lucky_number: int, numbers: tuple) -> int:
    good_pairs_count = 0
    prefix_sums = create_prefix_sums(numbers)

    end = 1
    for start in range(len(prefix_sums)):
        while end < len(prefix_sums) \
                and (prefix_sums[end] - prefix_sums[start] <= lucky_number):

            if prefix_sums[end] - prefix_sums[start] == lucky_number:
                good_pairs_count += 1
            end += 1

    return good_pairs_count


def main():
    numbers_count, lucky_number = map(int, input().split())
    numbers = tuple(map(int, input().split()))

    result = get_number_pairs_count(lucky_number, numbers)
    print(result)


if __name__ == '__main__':
    main()
