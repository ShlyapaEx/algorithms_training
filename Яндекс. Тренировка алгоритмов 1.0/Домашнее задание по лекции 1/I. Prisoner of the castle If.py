# https://contest.yandex.ru/contest/27393/problems/I/
# Решение на основе разбора: https://www.youtube.com/watch?v=mdJdB7On4AM&list=PL6Wui14DvQPySdPv5NUqV3i8sDbHkCKC5&index=5

def main():
    brick, hole = sorted([int(input()) for _ in range(3)]), \
        sorted([int(input()) for _ in range(2)])
    if hole[0] >= brick[0] and hole[1] >= brick[1]:
        return "YES"
    return "NO"


if __name__ == '__main__':
    print(main())
