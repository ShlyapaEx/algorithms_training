# https://contest.yandex.ru/contest/27794/problems/A/

import random
import time


def stress_test():

    tshirts = sorted(
        list(set([random.randint(1, 10_000_000) for i in range(100_000)])))
    pants = sorted(
        list(set([random.randint(1, 10_000_000) for i in range(100_000)])))
    start_time = time.time()
    result = get_most_stylish_pair(tshirts, pants)
    end_time = time.time()
    print(end_time - start_time)
    print(result)


def compare_test():
    while True:
        tshirts = sorted(
            list(set([random.randint(1, 100) for i in range(10)])))
        pants = sorted(
            list(set([random.randint(1, 100) for i in range(10)])))

        slow_result = slow_get_most_stylish_pair(tshirts, pants)
        fast_result = get_most_stylish_pair(tshirts, pants)

        if slow_result != fast_result:
            print("ERROR!")
            print(f"tshirts: {tshirts}")
            print(f"pants: {pants}")

            print(f"actual result: {slow_result}")
            print(f"got result: {fast_result}")
            break


def slow_get_most_stylish_pair(tshirts: tuple[int], pants: tuple[int]):
    best_tshirt = tshirts[0]
    best_pants = pants[0]
    min_diff = abs(tshirts[0] - pants[0])
    best_pants_index = 0

    for start in range(len(tshirts)):
        end = best_pants_index
        while end < len(pants) and min_diff > 0:
            pair_style = abs(tshirts[start] - pants[end])
            if pair_style < min_diff:
                best_tshirt = tshirts[start]
                best_pants = pants[end]
                best_pants_index = end
                min_diff = pair_style
            end += 1

    return best_tshirt, best_pants

# TODO: Дорешать


def get_most_stylish_pair(tshirts: tuple[int], pants: tuple[int]):
    best_tshirt = tshirts[0]
    best_pants = pants[0]
    min_diff = abs(tshirts[0] - pants[0])
    best_pants_index = 0
    prev_pair_style = min_diff
    for start in range(len(tshirts)):
        end = best_pants_index
        while end < len(pants) and min_diff > 0:
            pair_style = abs(tshirts[start] - pants[end])
            if pair_style > prev_pair_style:
                break
            if pair_style < min_diff:
                best_tshirt = tshirts[start]
                best_pants = pants[end]
                best_pants_index = end
                min_diff = pair_style
            prev_pair_style = pair_style
            end += 1

    return best_tshirt, best_pants


def main():
    tshirts_count = int(input())
    tshirts = tuple(map(int, input().split()))
    pants_count = int(input())
    pants = tuple(map(int, input().split()))

    result = get_most_stylish_pair(tshirts, pants)
    print(*result)


if __name__ == '__main__':
    compare_test()
