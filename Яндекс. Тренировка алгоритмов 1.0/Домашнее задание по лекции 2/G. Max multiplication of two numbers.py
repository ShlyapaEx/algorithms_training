# https://contest.yandex.ru/contest/27472/problems/G/

# import random


# def test():
#     while True:
#         randomlist = random.sample(range(-15, 15), 5)
#         print(f"Пробуем список: {randomlist}")
#         slow_result = bad_search_greatest(randomlist)
#         fast_result = search_greatest_multiplication(randomlist)
#         if list(slow_result) != list(fast_result):
#             print("НАШЛАСЬ ОШИБКА")
#             print(f"Ожидалось: {slow_result}, а получили {fast_result}")
#             break

# # Выдаёт не всегда правильное решение, но немного помогла мне :)
# def bad_search_greatest(numbers: list[int]):
#     max_multiplication = numbers[0] * numbers[1]
#     num_1, num_2 = numbers[0], numbers[1]
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] * numbers[j] > max_multiplication:
#                 max_multiplication = numbers[i] * numbers[j]
#                 num_1, num_2 = numbers[i], numbers[j]
#     return sorted((num_1, num_2))


def search_greatest_multiplication(numbers: list[int]):
    max_1, max_2 = max(numbers[0], numbers[1]), min(numbers[0], numbers[1])
    min_1, min_2 = max_2, max_1
    for i in range(2, len(numbers)):
        if numbers[i] >= max_1:
            max_2 = max_1
            max_1 = numbers[i]
        elif numbers[i] >= max_2:
            max_2 = numbers[i]
        if numbers[i] <= min_1:
            min_2 = min_1
            min_1 = numbers[i]
        elif numbers[i] <= min_2:
            min_2 = numbers[i]
    if (max_1 * max_2) > (min_1 * min_2):
        return (max_2, max_1)
    return (min_1, min_2)


def main():
    numbers = list(map(int, input().split()))
    print(*search_greatest_multiplication(numbers))


if __name__ == '__main__':
    # test()
    main()
