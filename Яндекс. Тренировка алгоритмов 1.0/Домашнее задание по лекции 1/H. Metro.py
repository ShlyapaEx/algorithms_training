# https://contest.yandex.ru/contest/27393/problems/G/
# # Решение на основе разбора: https://www.youtube.com/watch?v=mdJdB7On4AM&list=PL6Wui14DvQPySdPv5NUqV3i8sDbHkCKC5&index=5

def get_min_and_max_time(interval: int, train_count: int):
    minimal_time = train_count + interval * (train_count - 1)
    maximal_time = minimal_time + 2 * interval
    return minimal_time, maximal_time


def main():
    first_interval, second_interval, \
        first_count, second_count = [int(input()) for _ in range(4)]
    first_min, first_max = get_min_and_max_time(first_interval, first_count)
    second_min, second_max = get_min_and_max_time(second_interval,
                                                  second_count)
    min_time = max(first_min, second_min)
    max_time = min(first_max, second_max)
    if min_time > max_time:
        return print(-1)
    return print(min_time, max_time)


if __name__ == '__main__':
    main()
