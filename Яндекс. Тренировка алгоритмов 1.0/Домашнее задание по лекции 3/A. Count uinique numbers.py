# https://contest.yandex.ru/contest/27663/problems/A/

def count_unique_numbers(numbers_string: str) -> int:
    unique_numbers = set(map(int, numbers_string.split()))
    return len(unique_numbers)


def main():
    numbers_string = input()
    print(count_unique_numbers(numbers_string))


if __name__ == '__main__':
    main()
