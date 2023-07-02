# https://contest.yandex.ru/contest/27665/problems/D/

from typing import Literal


def get_keyboard_condition(buttons_durability: tuple[int], pressed_buttons: tuple[int]) -> list[Literal['YES', 'NO']]:
    result = []
    buttons_pressed_limit = {}
    for i in range(len(buttons_durability)):
        buttons_pressed_limit[i + 1] = buttons_durability[i]

    for button in pressed_buttons:
        buttons_pressed_limit[button] -= 1

    for value in buttons_pressed_limit.values():
        if value < 0:
            result.append('YES')
        else:
            result.append('NO')
    return result


def main():
    buttons_count = int(input())
    buttons_durability = tuple(map(int, input().split()))
    pressed_buttons_count = int(input())
    pressed_buttons = tuple(map(int, input().split()))

    result = get_keyboard_condition(buttons_durability, pressed_buttons)

    for i in range(len(result)):
        print(result[i])


if __name__ == '__main__':
    main()
