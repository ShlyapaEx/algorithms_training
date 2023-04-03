# https://contest.yandex.ru/contest/27393/problems/I/


def try_sides(side1, side2, hole_side1, hole_side2):

    if (side1 <= hole_side1 and side2 <= hole_side2) or \
            (side1 <= hole_side2 and side2 <= hole_side1):
        return True
    return False


def main():
    A, B, C, D, E = [int(input()) for _ in range(5)]

    try1 = try_sides(A, B, D, E)
    try2 = try_sides(A, C, D, E)
    try3 = try_sides(B, C, D, E)

    if any((try1, try2, try3)):
        return "YES"
    return "NO"


if __name__ == '__main__':
    print(main())
