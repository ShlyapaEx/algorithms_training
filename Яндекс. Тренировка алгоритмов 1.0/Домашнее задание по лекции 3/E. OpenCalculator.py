# https://contest.yandex.ru/contest/27663/problems/E/

def get_unique_digits(number: int) -> set[int]:
    unique_digits = set()
    while number > 0:
        last_digit = number % 10
        unique_digits.add(last_digit)
        number = number // 10
    return unique_digits


def open_calculator(buttons: str, number: int):
    buttons = set(map(int, buttons.split()))
    unique_digits = get_unique_digits(number)

    add_buttons_count = 0
    for digit in unique_digits:
        if digit not in buttons:
            add_buttons_count += 1
    return add_buttons_count


def main():
    buttons, number = input(), int(input())
    result = open_calculator(buttons, number)
    print(result)

if __name__ == '__main__':
    main()
