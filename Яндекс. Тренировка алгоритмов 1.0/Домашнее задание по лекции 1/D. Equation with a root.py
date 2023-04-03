# https://contest.yandex.ru/contest/27393/problems/D/

def main():
    a, b, c = [int(input()) for _ in range(3)]
    if c < 0:
        return "NO SOLUTION"
    if a == 0:
        if c ** 2 == b:
            return "MANY SOLUTIONS"
        return "NO SOLUTION"

    x = (c ** 2 - b) / a
    if int(x) == x:
        return int(x)
    return "NO SOLUTION"


if __name__ == '__main__':
    print(main())
