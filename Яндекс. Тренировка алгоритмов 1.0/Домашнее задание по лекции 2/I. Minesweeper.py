# https://contest.yandex.ru/contest/27472/problems/I/
#

def create_field(lines: int, rows: int, mines: int):
    field = [[0 for x in range(rows)] for y in range(lines)]
    print(field)


def main():
    lines, rows, mines = map(int, input().split())
    create_field(lines, rows, mines)


if __name__ == '__main__':
    print(main())
