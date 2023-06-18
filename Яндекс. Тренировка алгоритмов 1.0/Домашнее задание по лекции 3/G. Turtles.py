# https://contest.yandex.ru/contest/27663/problems/G/

def get_honest_turtles(turtles_count: int, turtle_sayings: set[str]) -> int:
    honest_turtles = 0
    for saying in turtle_sayings:
        turtles_ahead, turtles_behind = map(int, saying.split())
        if (turtles_ahead + turtles_behind == turtles_count - 1) \
                and (turtles_ahead >= 0) and (turtles_behind >= 0):
            honest_turtles += 1
    return honest_turtles


def main():
    turtles_count = int(input())
    turtle_sayings = set()
    for _ in range(turtles_count):
        turtle_sayings.add(input())

    honest_turtles = get_honest_turtles(turtles_count, turtle_sayings)
    print(honest_turtles)


if __name__ == '__main__':
    main()
