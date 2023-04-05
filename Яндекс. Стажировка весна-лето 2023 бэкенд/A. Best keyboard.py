# https://contest.yandex.ru/contest/44525/problems/A/

# Версия 1. Валится из-за ошибки TL

def get_symbol_row(symbol_index: int, symbols_rows: list[int]):
    return symbols_rows[symbol_index]


def main():
    int(input())
    symbols = tuple(map(int, input().split()))
    symbols_rows = list(map(int, input().split()))
    int(input())
    referat = list(map(int, input().split()))

    result = 0
    current_row = get_symbol_row(symbols.index(referat[0]),
                                 symbols_rows)

    for symbol in referat:
        next_symbol_row = get_symbol_row(symbols.index(symbol), symbols_rows)
        if next_symbol_row != current_row:
            result += 1
        current_row = next_symbol_row
    return result


if __name__ == '__main__':
    print(main())
