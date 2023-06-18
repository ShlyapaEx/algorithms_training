# https://contest.yandex.ru/contest/27472/problems/F/
# Подсмотрел решение здесь: https://github.com/Yankovsky/yandex-algos-training/blob/master/hw2/f.py

def is_symmetric(numbers: list[int]):
    for i in range(len(numbers) // 2):
        if numbers[i] != numbers[-i - 1]:
            return False
    return True


def symmetric_sequence(numbers: list[int]):
    for i in range(len(numbers)):
        if is_symmetric(numbers[i:]):
            return list(reversed(numbers[:i]))


def main():
    n = int(input())
    numbers = list(map(int, input().split()))
    added_part = symmetric_sequence(numbers)
    print(len(added_part))
    if added_part:
        print(*added_part)


if __name__ == '__main__':
    main()
