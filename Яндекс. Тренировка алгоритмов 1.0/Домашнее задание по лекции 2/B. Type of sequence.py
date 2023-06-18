# https://contest.yandex.ru/contest/27472/problems/B/

def is_constant(number_list: list[int]):
    if len(set(number_list)) == 1:
        return True
    return False


def is_ascending(number_list: list[int]):
    for i in range(len(number_list) - 1):
        if number_list[i + 1] <= number_list[i]:
            return False
    return True


def is_weakly_ascending(number_list: list[int]):
    for i in range(len(number_list) - 1):
        if number_list[i + 1] < number_list[i]:
            return False
    return True


def is_descending(number_list: list[int]):
    for i in range(len(number_list) - 1):
        if number_list[i + 1] >= number_list[i]:
            return False
    return True


def is_weakly_descending(number_list: list[int]):
    for i in range(len(number_list) - 1):
        if number_list[i + 1] > number_list[i]:
            return False
    return True


def main():
    input_number = int(input())
    number_list = []
    while input_number != -2000000000:
        number_list.append(input_number)
        input_number = int(input())

    if is_constant(number_list):
        return "CONSTANT"
    if is_ascending(number_list):
        return "ASCENDING"
    if is_weakly_ascending(number_list):
        return "WEAKLY ASCENDING"
    if is_descending(number_list):
        return "DESCENDING"
    if is_weakly_descending(number_list):
        return "WEAKLY DESCENDING"
    return "RANDOM"


if __name__ == '__main__':
    print(main())
